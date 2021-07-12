import uuid

from django.contrib.postgres.fields                     import ArrayField
from django.db                                          import models

from zigida.core.model_mixins                           import AuditFields
from zigida.common.global_choices                       import APP_TYPE
from zigida.core.utils                                  import randcode_gen


# Create your models here.
def default_pages():
    return []


class Visitor(models.Model):

    uuid_code        = models.UUIDField('ID', primary_key=True,    default=uuid.uuid4,     editable=False,            null=False)

    location         = models.ForeignKey('locations.Location',   on_delete=models.PROTECT, related_name='visitors',     null=True)

    token_key        = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False,    blank=True,                     null=True)
    code             = models.CharField('CODE',             max_length=100,             blank=False,    default=randcode_gen)

    pages_arrary     = ArrayField(models.CharField('PAGES', max_length=9999),           default=default_pages,          null=True)
    language         = models.CharField('LANGUAGE',         max_length=2,                                               null=True)
    app_type         = models.CharField('APP TYPE',         max_length=3,               choices=APP_TYPE,               null=True)
    date_created     = models.DateField('DATE CREATED',     auto_now_add=True)
    datetime_updated = models.DateTimeField('DATE UPDATED', auto_now=True)
    last_updated_by  = models.CharField('LAST UPDATED BY',  max_length=50,          blank=True,                         null=True)
    bool_deleted     = models.BooleanField('IS DELETED?',                           default=False)

    class Meta:

        app_label   = 'visitors'
        db_table    = 'visitors'
        verbose_name_plural = 'visitors'
