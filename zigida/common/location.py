from django.conf                                                import settings
from django.db.models                                           import Q

from zigida.common.device                                       import get_device_info
from zigida.apps.db.locations.models                            import Location


def get_location(i):

    location = Location.objects \
        .filter(
            user_id = i['user_uuid_code']
        ) \
        .exclude(
            Q(bool_active   = False) |
            Q(bool_deleted  = True)
        ) \
        .values(
            'uuid_code', 'code', 'ipaddress', 'macaddress', 'street', 'city', 'zip_code', 'region', 'country_code',
            'country_name', 'lat', 'lng', 'phone_number', 'area_code', 'mcc', 'mnc', 'mobile_brand', 'device_type',
            'device_model', 'op_system', 'isp', 'domain', 'timezone', 'netspeed', 'idd_code', 'usage_type',
            'weather_code', 'weather_name', 'bool_active', 'datetime_created', 'datetime_updated', 'last_updated_by',
            'bool_deleted'
        ) \
        .first()

    return location


def get_locations(i, **kwargs):

    if i:
        request = i.get('request')

    locations = Location.objects \
        .exclude(
            Q(bool_active  = False) |
            Q(bool_deleted = True)
        ) \
        # .values(
        #     'uuid_code', 'code', 'ipaddress', 'macaddress', 'street', 'city', 'zip_code', 'region', 'country_code',
        #     'country_name', 'lat', 'lng', 'phone_number', 'area_code', 'mcc', 'mnc', 'mobile_brand', 'device_type',
        #     'device_model', 'op_system', 'isp', 'domain', 'timezone', 'netspeed', 'idd_code', 'usage_type',
        #     'weather_code', 'weather_name', 'bool_active', 'datetime_created', 'datetime_updated', 'last_updated_by',
        #     'bool_deleted'
        # )

    ip_data  = kwargs.get('ip_data')

    location = None

    if ip_data:
        if ip_data.get('ip') and ip_data.get('city'):
            location = locations \
                .filter(
                    Q(ipaddress = ip_data.get('ip')) &
                    Q(city      = ip_data.get('city'))
                  ) \
                .first()

    return location


def create_location(i, request, **kwargs):

    ip_data       = kwargs.get('ip_data')
    user          = kwargs.get('user')
    timezone      = ''
    user_fullname = None

    if ip_data:
        timezone    = ip_data.get('timezone')
        user_fullname = ip_data.get('ip')

    if user:
        user_fullname = user.fullname

    if not timezone:
        timezone = settings.TIME_ZONE

    device = get_device_info(request)

    location_first = get_locations(i, ip_data=ip_data)

    location = Location()

    if location_first:
        location = location_first

    location.ipaddress      = ip_data.get('ip')
    location.macaddress     = ''
    location.street         = ''
    location.city           = ip_data.get('city')
    location.zip_code       = ip_data.get('postal')
    location.region         = ip_data.get('region')
    location.country_code   = ip_data.get('country')
    location.country_name   = ip_data.get('country_name')
    location.lat            = ip_data.get('latitude')
    location.lng            = ip_data.get('longitude')
    location.phone_number   = ''
    location.area_code      = ''
    location.mcc            = ''
    location.mnc            = ''
    location.mobile_brand   = device.get('model')
    location.device_type    = device.get('type')
    location.device_model   = device.get('model')
    location.op_system      = device.get('os')
    location.isp            = ip_data.get('org')
    location.domain         = ''
    location.timezone       = timezone
    location.netspeed       = ''
    location.idd_code       = ''
    location.usage_type     = device.get('browser')
    location.weather_code   = ''
    location.weather_name   = ''

    location.last_updated_by = user_fullname

    location.save()

    return location


def update_location(i, request, **kwargs):

    ip_data  = kwargs.get('ip_data')
    user   = kwargs.get('user')
    timezone = ip_data.get('timezone')

    user_fullname = i['user_fullname']

    if user:
        user_fullname = user.fullname

    if not timezone:
        timezone = settings.TIME_ZONE

    device = get_device_info(request)

    location = get_location(i)

    location.ipaddress      = ip_data.get('ip')
    location.macaddress     = ''
    location.street         = ''
    location.city           = ip_data.get('city')
    location.zip_code       = ip_data.get('postal')
    location.region         = ip_data.get('region')
    location.country_code   = ip_data.get('country')
    location.country_name   = ip_data.get('country_name')
    location.lat            = ip_data.get('latitude')
    location.lng            = ip_data.get('longitude')
    location.phone_number   = ''
    location.area_code      = ''
    location.mcc            = ''
    location.mnc            = ''
    location.mobile_brand   = device.get('model')
    location.device_type    = device.get('type')
    location.device_model   = device.get('model')
    location.op_system      = device.get('os')
    location.isp            = ip_data.get('org')
    location.domain         = ''
    location.timezone       = timezone
    location.netspeed       = ''
    location.idd_code       = ''
    location.usage_type     = device.get('browser')
    location.weather_code   = ''
    location.weather_name   = ''

    location.last_updated_by = user_fullname

    location.save()

    return location
