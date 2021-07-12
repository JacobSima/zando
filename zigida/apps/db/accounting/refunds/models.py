import uuid

from django.conf                                                import settings
from django.db                                                  import models

from zigida.common.global_choices                               import REFUND_STATUS
from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import refund_randcode_gen


# Create your models here.
class Refund(AuditFields):

    uuid_code       = models.UUIDField('ID', primary_key=True,    default=uuid.uuid4,     editable=False,             null=False)

    customer        = models.ForeignKey(settings.AUTH_USER_MODEL,       on_delete=models.PROTECT, related_name='refunds')
    item            = models.OneToOneField('items.Item',    on_delete=models.PROTECT,   related_name='refunds',         null=True)
    location        = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='refunds',       null=True)

    token_key       = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False,             blank=True,             null=True)
    code            = models.CharField('CODE',          max_length=100,                 blank=False,  default=refund_randcode_gen)

    phone_number    = models.CharField('PHONE NUMBER',  max_length=50,                          blank=True,             null=True)
    email           = models.EmailField('EMAIL',        blank=True,             null=True)
    reason          = models.TextField('REASON',        blank=True,             null=True)
    refund_status   = models.BooleanField('REFUND STATUS',                      choices=REFUND_STATUS,                  null=True)

    class Meta:

        app_label   = 'refunds'
        db_table    = 'refunds'
        verbose_name_plural = 'refunds'
