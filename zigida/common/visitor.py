from django.db.models                                   import Q
from django.utils                                       import timezone

from zigida.common                                      import location as location_lib
from zigida.apps.db.visitors.models                     import Visitor


def get_visitor(ip_data, **kwargs):

    # ip_data = kwargs.get('ip_data')
    i = kwargs.get('i')

    visitors = Visitor.objects \
        .exclude(
            Q(bool_deleted = True)
        ) \
        # .values(
        #     'uuid_code', 'token_key', 'code', 'pages_arrary', 'language', 'app_type',
        #     'location_id',
        #
        #     'location__code', 'location__ipaddress', 'location__macaddress', 'location__street',
        #     'location__city', 'location__zip_code', 'location__region',  'location__country_code', 'location__country_name',
        #     'location__lat', 'location__lng', 'location__phone_number', 'location__area_code',  'location__mcc',
        #     'location__mnc', 'location__mobile_brand', 'location__device_type', 'location__device_model',
        #     'location__op_system',  'location__isp', 'location__domain', 'location__timezone', 'location__netspeed',
        #     'location__idd_code', 'location__usage_type',  'location__weather_code', 'location__weather_name',
        #     'location__bool_active', 'location__datetime_created', 'location__datetime_updated', 'location__last_updated_by',
        #     'location__bool_deleted'
        # )

    visitor = None
    if ip_data.get('ip') and ip_data.get('city') and ip_data.get('country'):
        visitor = visitors \
            .filter(
                Q(language                        = i.get('lang')) &
                Q(date_created__gte               = timezone.now().date()) &
                Q(location__ipaddress             = ip_data.get('ip')) &
                Q(location__city                  = ip_data.get('city')) &
                Q(location__country_code          = ip_data.get('country'))
            ) \
            .first()

    return visitor


def create_visitor(i, request, ip_data, **kwargs):

    location = location_lib.create_location(i, request, ip_data=ip_data)

    visitor_first = get_visitor(ip_data, i=i, **kwargs)

    pages_array = []
    page_link   = i.get('page_link')
    location_id = location.uuid_code

    visitor     = Visitor()

    if visitor_first:
        visitor         = visitor_first
        i['lang']       = i.get('lang')     if i['lang'] else visitor.language
        pages_array     = visitor.pages_arrary  if visitor.pages_arrary else pages_array
        i['app_type']   = i.get('app_type')     if i['app_type'] else visitor.app_type
        location_id     = visitor.location_id

    pages_array.append(page_link)

    visitor.location_id     = location_id
    visitor.pages_arrary    = pages_array
    visitor.language        = i.get('lang')
    visitor.app_type        = i.get('app_type')
    visitor.last_updated_by = ip_data.get('ip')

    visitor.save()

    return visitor
