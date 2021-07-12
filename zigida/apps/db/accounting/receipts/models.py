import uuid

from django.conf                                                import settings
from django.db                                                  import models

from zigida.common.global_choices                               import PAYMENT_TYPE
from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import receipt_randcode_gen


# Create your models here.
class Receipt(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    customer            = models.ForeignKey(settings.AUTH_USER_MODEL,       on_delete=models.PROTECT, related_name='receipts')
    location            = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='receipts',  null=True)
    payment             = models.OneToOneField('payments.Payment',  on_delete=models.PROTECT, related_name='receipts',  null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=receipt_randcode_gen)

    amount              = models.DecimalField('AMOUNT',             decimal_places=5,   max_digits=15, default=0.00,    null=True)
    payment_type        = models.CharField('PAYMENT TYPE',          choices=PAYMENT_TYPE,   max_length=2,               null=True)

    class Meta:
        app_label   = 'receipts'
        db_table    = 'receipts'
        verbose_name_plural = 'receipts'
