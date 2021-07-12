import uuid

from django.db                                                  import models

from zigida.core.model_mixins                                   import AuditFields
from zigida.core.utils                                          import color_randcode_gen


# Create your models here.
class Color(AuditFields):

    uuid_code           = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    token_key           = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code                = models.CharField('CODE',                  max_length=100,     blank=False, default=color_randcode_gen)

    title               = models.CharField('TITLE',                 max_length=250,     blank=True,                     null=True)
    shade               = models.CharField('SHADE',                 max_length=250,     blank=True,                     null=True)
    Description         = models.TextField('DESCRIPTION',                               blank=True,                     null=True)

    class Meta:
        app_label   = 'colors'
        db_table    = 'colors'
        verbose_name_plural = 'colors'
