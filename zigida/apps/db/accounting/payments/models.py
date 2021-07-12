import uuid
from decimal                                                    import Decimal

from django.conf                                                import settings
from django.core.validators                                     import MinValueValidator
from django.db                                                  import models

from zigida.common.global_choices                               import PAYMENT_TYPE, CARD_TYPE, MOBILE_MONEY_TYPE
from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import pay_randcode_gen


# Create your models here.
class Payment(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    customer            = models.ForeignKey(settings.AUTH_USER_MODEL,       on_delete=models.PROTECT, related_name='payments')
    bank                = models.ForeignKey('banks.Bank',           on_delete=models.PROTECT, related_name='payments',  null=True)
    location            = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='payments',  null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=pay_randcode_gen)

    mpesa_charge_id     = models.CharField('MPESA PAY ID',          max_length=100,                     blank=True,     null=True)
    paypal_charge_id    = models.CharField('PAYPAL PAY ID',         max_length=100,                     blank=True,     null=True)
    stripe_charge_id    = models.CharField('STRIPE PAY ID',         max_length=100,                     blank=True,     null=True)

    amount_paid         = models.DecimalField('AMOUNT PAID',        decimal_places=5,       max_digits=15,
                                            validators=[MinValueValidator(Decimal(0.00))],  default=0.00,               null=True)
    amount_outstanding  = models.DecimalField('OUTSTANDING AMOUNT', decimal_places=5,       max_digits=15,
                                            validators=[MinValueValidator(Decimal(0.00))],  default=0.00,               null=True)
    payment_type        = models.CharField('PAYMENT TYPE',          max_length=1, choices=PAYMENT_TYPE,      blank=True,null=True)
    card_type           = models.CharField('CARD TYPE',             max_length=1, choices=CARD_TYPE,         blank=True,null=True)
    mob_money_type      = models.CharField('MOBILE MONEY TYPE',     max_length=1, choices=MOBILE_MONEY_TYPE, blank=True,null=True)

    class Meta:
        app_label   = 'payments'
        db_table    = 'payments'
        verbose_name_plural = 'payments'
