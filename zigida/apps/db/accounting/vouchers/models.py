import uuid
from decimal                                            import Decimal

from django.conf                                        import settings
from django.contrib.postgres.fields                     import ArrayField
from django.core.validators                             import MinValueValidator
from django.db                                          import models

from zigida.core.model_mixins                           import AuditFields
from zigida.core.utils                                  import randcode_gen


def default_voucher():
    return []


# Create your models here.
class Voucher(AuditFields):

    uuid_code       = models.UUIDField('ID', primary_key=True,    default=uuid.uuid4,     editable=False,           null=False)

    customer        = models.ForeignKey(settings.AUTH_USER_MODEL,   on_delete=models.PROTECT, related_name='vouchers')
    location        = models.ForeignKey('locations.Location',  on_delete=models.PROTECT, related_name='vouchers',   null=True)

    item_arrary     = ArrayField(models.CharField('ITEMS',              max_length=9999), default=default_voucher,  null=True)
    order_arrary    = ArrayField(models.CharField('ORDERS',             max_length=9999), default=default_voucher,  null=True)
    payment_arrary  = ArrayField(models.CharField('PAYMENTS',           max_length=9999), default=default_voucher,  null=True)

    token_key       = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False,             blank=True,         null=True)
    code            = models.CharField('CODE',          max_length=100,             blank=False,    default=randcode_gen)

    amount          = models.DecimalField('VOUCHER AMOUNT',
                    decimal_places=5, max_digits=15, validators=[MinValueValidator(Decimal(0.00))], default=0.00,   null=True)

    class Meta:

        app_label   = 'vouchers'
        db_table    = 'vouchers'
        verbose_name_plural = 'vouchers'
