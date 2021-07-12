import uuid

from django.conf                                                import settings
from django.db                                                  import models

from django_countries.fields                                    import CountryField

from zigida.common.global_choices                               import ADDRESS_CHOICES
from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import randcode_gen


# Create your models here.
class Address(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4,       editable=False,           null=False)

    customer            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='addresses')
    location            = models.ForeignKey('locations.Location', on_delete=models.PROTECT, related_name='addresses',   null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=randcode_gen)

    street_address      = models.CharField('STREET NAME',           max_length=100,     blank=True,                     null=True)
    apartment_address   = models.CharField('HOME NUMBER',           max_length=100,     blank=True,                     null=True)
    country             = CountryField('COUNTRY CODE',              multiple=False,     blank=True,                     null=True)
    zipcode             = models.CharField('POSTAL',                max_length=100,     blank=True,                     null=True)
    address_type        = models.CharField('ADDRESS TYPE',          max_length=1, choices=ADDRESS_CHOICES, blank=True,  null=True)
    payment_option      = models.CharField('PAYMENT OPTION',        max_length=100,     blank=True,                     null=True)

    default             = models.BooleanField('DEFAULT ADDRESS',    default=False,      blank=True,                     null=True)

    class Meta:
        app_label   = 'addresses'
        db_table    = 'addresses'
        verbose_name_plural = 'addresses'
