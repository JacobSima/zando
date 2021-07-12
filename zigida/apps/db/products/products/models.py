import os
import uuid

from django.conf                                                import settings
from django.contrib.postgres.fields                             import ArrayField
from django.db                                                  import models
from django.dispatch                                            import receiver

from zigida.core.model_mixins                                   import AuditFields, ProductStockFields
from zigida.core.utils                                          import prod_randcode_gen, unique_slug_generator


def categories_array():
    return []

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def products_img_path(instance, filename):

    full_path       = settings.FUTACASH_DIR
    new_filename    = instance.code
    name, ext       = get_filename_ext(filename)
    finale_filename = f'{new_filename}{ext}'

    if os.path.exists(f"{full_path}/products"):
        os.chdir(f"{full_path}/products")
        for file in os.listdir("."):
            if os.path.isfile(file) and file.startswith(f"{finale_filename}"):
                try:
                    os.remove(file)
                except Exception as e:
                    print(e)

    return "products/{finale_filename}".format(new_filename=new_filename, finale_filename=finale_filename)


# Create your models here.
class Product(AuditFields, ProductStockFields):

    uuid_code       = models.UUIDField('ID',  primary_key=True, default=uuid.uuid4, editable=False,                 null=False)

    # category        = models.ForeignKey('stores.Store',         on_delete=models.PROTECT, related_name='products',  null=True)
    # color           = models.ForeignKey('colors.Color',         on_delete=models.PROTECT, related_name='products',  null=True)
    store           = models.ForeignKey('stores.Store',         on_delete=models.PROTECT, related_name='products',  null=True)
    # size            = models.ForeignKey('sizes.Size',           on_delete=models.PROTECT, related_name='products',  null=True)

    token_key       = models.UUIDField('TOKEN',     default=uuid.uuid4,             editable=False, blank=True,     null=True)
    code            = models.CharField('CODE',                  max_length=100,     blank=False,    default=prod_randcode_gen)

    title           = models.CharField('TITLE',                 max_length=250,                     blank=True,     null=True)
    slug            = models.SlugField('SLUG',                  unique=True,                        blank=True,     null=True)
    image           = models.ImageField('PRODUCT IMAGE',        upload_to=products_img_path,        blank=True,     null=True)
    description     = models.TextField('DESCRIPTION',                                               blank=True,     null=True)

    price           = models.DecimalField('PRICE',              max_digits=19,      default=0,  decimal_places=2,  blank=True)
    discount_price  = models.DecimalField('DISCOUNTED PRICE',   max_digits=19,      default=0,  decimal_places=2,  blank=True)
    label           = models.CharField('TITLE',                 max_length=250,                 blank=True,         null=True)
    category        = ArrayField(models.CharField('CATEGORY',   max_length=999),    default=categories_array,       null=True)
    color           = ArrayField(models.CharField('COLOR',      max_length=999),    default=categories_array,       null=True)
    size            = ArrayField(models.CharField('SIZE',       max_length=999),    default=categories_array,       null=True)

    class Meta:
        app_label   = 'products'
        db_table    = 'products'
        verbose_name_plural = 'products'


@receiver(models.signals.pre_save, sender=Product)
def prod_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
