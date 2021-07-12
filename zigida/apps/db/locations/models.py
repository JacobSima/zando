import uuid

from django.db                                          import models

from zigida.core.model_mixins                           import AuditFields
from zigida.core.utils                                  import randcode_gen


# Create your models here.
class Location(AuditFields):

    uuid_code       = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False,    null=False)
    code            = models.CharField('CODE', max_length=100, blank=False, default=randcode_gen)

    ipaddress       = models.GenericIPAddressField('IP ADDRESS',            blank=True, null=True)
    macaddress      = models.CharField('MAC ADDRESS',   max_length=100,     blank=True, null=True)

    street          = models.CharField('STREET',        max_length=100,     blank=True, null=True)
    city            = models.CharField('CITY',          max_length=100,     blank=True, null=True)
    zip_code        = models.CharField('POST CODE',     max_length=100,     blank=True, null=True)
    region          = models.CharField('REGION',        max_length=100,     blank=True, null=True)
    country_code    = models.CharField('COUNTRY CODE.',  max_length=100,     blank=True, null=True)
    country_name    = models.CharField('COUNTRY NAME',  max_length=100,     blank=True, null=True)

    lat             = models.CharField('LATITUDE',      max_length=100,     blank=True, null=True)
    lng             = models.CharField('LONGITUDE',     max_length=100,     blank=True, null=True)

    phone_number    = models.CharField('PHONE',         max_length=100,     blank=True, null=True)
    area_code       = models.CharField('AREA CODE',     max_length=100,     blank=True, null=True)
    mcc             = models.CharField('MCC',           max_length=100,     blank=True, null=True)
    mnc             = models.CharField('MNC',           max_length=100,     blank=True, null=True)
    mobile_brand    = models.CharField('MOBILE BRAND',  max_length=100,     blank=True, null=True)

    device_type     = models.CharField('DEVICE TYPE',   max_length=100,     blank=True, null=True)
    device_model    = models.CharField('DEVICE MODEL',  max_length=100,     blank=True, null=True)
    op_system       = models.CharField('OPERAT. SYS',   max_length=100,     blank=True, null=True)

    isp             = models.CharField('ISP',           max_length=100,     blank=True, null=True)
    domain          = models.CharField('DOMAIN',        max_length=100,     blank=True, null=True)
    timezone        = models.CharField('TIMEZONE',      max_length=100,     blank=True, null=True)
    netspeed        = models.CharField('NET SPEED',     max_length=100,     blank=True, null=True)
    idd_code        = models.CharField('IDD CODE',      max_length=100,     blank=True, null=True)
    usage_type      = models.CharField('USAGE TYPE',    max_length=100,     blank=True, null=True)

    weather_code    = models.CharField('WEATHER CODE',  max_length=100,     blank=True, null=True)
    weather_name    = models.CharField('WEATHER NAME',  max_length=100,     blank=True, null=True)

    bool_active     = models.BooleanField('IS ACTIVE', default=True)

    class Meta:

        app_label   = 'locations'
        db_table    = 'locations'
        verbose_name_plural = 'locations'

    @property
    def get_country(self):
        return self.country_code

    @property
    def get_city(self):
        return self.city
