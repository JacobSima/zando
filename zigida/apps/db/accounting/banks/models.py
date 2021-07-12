import uuid

from django.db                                                  import models

from zigida.core.model_mixins                                   import AuditFields, AddressFields
from zigida.core.utils                                          import bank_randcode_gen


# Create your models here.
class Bank(AuditFields, AddressFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=bank_randcode_gen)

    name                = models.CharField('NAME',                  max_length=100,     blank=True,                     null=True)
    swift_code          = models.CharField('SWIFT CODE',            max_length=100,     blank=True,                     null=True)

    bool_active         = models.BooleanField('IS ACTIVE',          default=True,       blank=True,                     null=True)

    class Meta:
        app_label   = 'banks'
        db_table    = 'banks'
        verbose_name_plural = 'banks'
