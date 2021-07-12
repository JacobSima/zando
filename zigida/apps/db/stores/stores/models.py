import uuid

from django.conf                                                import settings
from django.contrib.postgres.fields                             import ArrayField
from django.db                                                  import models

from zigida.core.model_mixins                                   import AuditFields, AddressFields
from zigida.core.utils                                          import store_randcode_gen


def employee_array():
    return []


# Create your models here.
class Store(AuditFields, AddressFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    customer            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='stores',  null=True)
    openinghour         = models.ForeignKey('openinghours.OpeningHour', on_delete=models.PROTECT, related_name='stores',null=True)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=store_randcode_gen)

    name                = models.CharField('NAME',                  max_length=100,     blank=True,                     null=True)
    employee            = ArrayField(models.CharField('EMPLOYEES',  max_length=999),    default=employee_array,         null=True)

    bool_active         = models.BooleanField('IS ACTIVE',          default=True,       blank=True,                     null=True)

    class Meta:
        app_label   = 'stores'
        db_table    = 'stores'
        verbose_name_plural = 'stores'
