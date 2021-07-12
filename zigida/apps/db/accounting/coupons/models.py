import uuid
from decimal                                                    import Decimal

from django.core.validators                                     import MinValueValidator
from django.db                                                  import models

from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import coup_randcode_gen


# Create your models here.
class Coupon(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=coup_randcode_gen)

    title               = models.CharField('TITLE',                 max_length=100,     blank=True,                     null=True)
    amount              = models.DecimalField('AMOUNT',             decimal_places=5,   max_digits=15,
                                                        validators=[MinValueValidator(Decimal(0.00))], default=0.00,    null=True)
    percent             = models.PositiveSmallIntegerField('PERCENT',default=0,         blank=True,                     null=True)
    date_from           = models.DateField('DATE FROM',                                 blank=True,                     null=True)
    date_to             = models.DateField('DATE TO',                                   blank=True,                     null=True)

    bool_active         = models.BooleanField('IS ACTIVE',          default=True,       blank=True,                     null=True)

    class Meta:
        app_label   = 'coupons'
        db_table    = 'coupons'
        verbose_name_plural = 'coupons'
