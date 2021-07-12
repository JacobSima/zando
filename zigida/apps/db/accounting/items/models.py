import uuid

from django.conf                                                import settings
from django.core.validators                                     import MinValueValidator, MaxValueValidator
from django.db                                                  import models

from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import item_randcode_gen


# Create your models here.
class Item(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    customer            = models.ForeignKey(settings.AUTH_USER_MODEL,       on_delete=models.PROTECT, related_name='items')
    # refund              = models.ForeignKey('refunds.Refund',       on_delete=models.PROTECT, related_name='items',     null=True)
    product             = models.ForeignKey('products.Product',     on_delete=models.PROTECT, related_name='items',     null=True)
    location            = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='items',     null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False,    default=item_randcode_gen)

    quantity            = models.PositiveSmallIntegerField('QUANTITY',
                                validators=[MinValueValidator(1), MaxValueValidator(999)], default=1,   blank=True,     null=True)

    price_buy           = models.DecimalField('PRICE BUY',              max_digits=19, default=0, decimal_places=2, blank=True)
    price_buy_original  = models.DecimalField('PRICE BUY ORIGINAL',     max_digits=19, default=0, decimal_places=2, blank=True)
    price_sell          = models.DecimalField('PRICE SELL',             max_digits=19, default=0, decimal_places=2, blank=True)
    price_sell_original = models.DecimalField('PRICE SELL ORIGINAL',    max_digits=19, default=0, decimal_places=2, blank=True)

    bool_active         = models.BooleanField('IS ACTIVE', default=True)

    class Meta:
        app_label   = 'items'
        db_table    = 'items'
        verbose_name_plural = 'items'
