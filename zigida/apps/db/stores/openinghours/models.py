import uuid

from django.db                                                  import models
# from django.utils.dates                                         import WEEKDAYS
from zigida.common.global_choices                               import WEEKDAYS
from zigida.core.model_mixins                                   import AuditFields, AddressFields
from zigida.core.utils                                          import randcode_gen


def employee_array():
    return []


# Create your models here.
class OpeningHour(AuditFields, AddressFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,     null=False)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4, editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',      max_length=100,     blank=False, default=randcode_gen)

    weekday             = models.PositiveSmallIntegerField('WEEK DAY',  choices=WEEKDAYS,   blank=True,     null=True)
    hour_from           = models.TimeField('HOUR FROM',                                     blank=True,     null=True)
    hour_to             = models.TimeField('HOUR FROM',                                     blank=True,     null=True)

    class Meta:
        app_label   = 'openinghours'
        db_table    = 'openinghours'
        verbose_name_plural = 'openinghours'
