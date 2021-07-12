import uuid

from django.db                                          import models

from zigida.common.global_choices                       import LANGUAGES
from zigida.core.model_mixins                           import AuditFields
from zigida.core.utils                                  import randcode_gen


# Create your models here.
class Email(AuditFields):

    uuid_code       = models.UUIDField('ID', primary_key=True,    default=uuid.uuid4,     editable=False,         null=False)

    user            = models.ForeignKey('sr_users.SRUser',      on_delete=models.PROTECT, related_name='emails',    null=True)
    location        = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='emails',    null=True)

    token_key       = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False,             blank=True,         null=True)
    code            = models.CharField('CODE',          max_length=100,                         blank=False, default=randcode_gen)

    sender          = models.CharField('SENDER',        max_length=100,                         blank=True,         null=True)
    receiver        = models.CharField('RECEIVER',      max_length=100,                         blank=True,         null=True)
    subject         = models.CharField('SUBJECT',       max_length=100,                         blank=True,         null=True)
    message         = models.CharField('MESSAGE',       max_length=250,                         blank=True,         null=True)
    language        = models.CharField('LANGUAGE',      max_length=3,                           choices=LANGUAGES,  default='FR')

    class Meta:

        app_label   = 'emails'
        db_table    = 'emails'
        verbose_name_plural = 'emails'
