import uuid

from django.conf                                                import settings
from django.db                                                  import models

from zigida.common.global_choices                               import PAYMENT_TYPE, ORDER_TYPE
from zigida.core.model_mixins                                   import AuditFields, OrdersDetailFields
from zigida.core.utils                                          import ord_randcode_gen


# Create your models here.
class Order(AuditFields, OrdersDetailFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    customer            = models.ForeignKey(settings.AUTH_USER_MODEL,       on_delete=models.PROTECT, related_name='orders')
    billing_address     = models.ForeignKey('addresses.Address', on_delete=models.SET_NULL,  related_name='billing_address',  null=True)
    shipping_address    = models.ForeignKey('addresses.Address', on_delete=models.SET_NULL,  related_name='shipping_address', null=True)
    coupon              = models.ForeignKey('coupons.Coupon',       on_delete=models.PROTECT,   related_name='orders',  null=True)
    location            = models.ForeignKey('locations.Location',   on_delete=models.PROTECT,   related_name='orders',  null=True)
    item                = models.ForeignKey('items.Item',           on_delete=models.PROTECT,   related_name='orders',  null=True)
    payment             = models.ForeignKey('payments.Payment',     on_delete=models.PROTECT,   related_name='orders',  null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=ord_randcode_gen)

    amount              = models.DecimalField('AMOUNT',             decimal_places=5,       max_digits=15, default=0.00,null=True)
    order_type          = models.CharField('ORDER TYPE',            choices=ORDER_TYPE,     max_length=2,               null=True)
    payment_type        = models.CharField('PAYMENT TYPE',          choices=PAYMENT_TYPE,   max_length=2,               null=True)

    class Meta:
        app_label   = 'orders'
        db_table    = 'orders'
        verbose_name_plural = 'orders'
