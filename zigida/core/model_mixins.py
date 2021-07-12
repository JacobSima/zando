from django.core.validators                             import MinValueValidator, MaxValueValidator
from django.db                                          import models
from django_countries.fields                            import CountryField

from zigida.common.global_choices                       import CURRENCIES


class AddressFields(models.Model):

    street_name     = models.CharField('Street Name', max_length=200,           blank=True,         null=True)
    house_number    = models.PositiveSmallIntegerField('Number',                blank=True,         null=True)
    post_code       = models.CharField('Postal Code', max_length=50,            blank=True,         null=True)
    area            = models.CharField('Area',        max_length=100,           blank=True,         null=True)
    city            = models.CharField('City',        max_length=100,           blank=True,         null=True)
    region          = models.CharField('Region',      max_length=100,           blank=True,         null=True)
    country         = CountryField('Country',                                                       null=True)

    class Meta:
        abstract = True


class AuditFields(models.Model):

    datetime_created    = models.DateTimeField('DATE CREATED',  auto_now_add=True)
    datetime_updated    = models.DateTimeField('DATE UPDATED',  auto_now=True)
    last_updated_by     = models.CharField('LAST UPDATED BY',   max_length=50,    blank=True,         null=True)
    bool_deleted        = models.BooleanField('IS DELETED?',    default=False)

    class Meta:
        abstract = True


class EmailFields(models.Model):

    email1          = models.EmailField('Admin. Email',                         blank=True,         null=True)
    email2          = models.EmailField('Account Email',                        blank=True,         null=True)
    email3          = models.EmailField('Branch Email',                         blank=True,         null=True)
    email4          = models.EmailField('Legal Email',                          blank=True,         null=True)

    class Meta:
        abstract = True


class OrdersDetailFields(models.Model):

    '''
        1. Item added to the cart
        2. Adding a billing address - (Handle Failed checkout)
        3. Payment - (Preprocessing, processing, packaging, etc ...)
        4. Item being delivered
        5. Item Received
        6. Refunds Requested
        7. Refunds Granted or Denied
    '''

    code_currency   = models.CharField('CURRENCY', choices=CURRENCIES,          max_length=3,       default='CDF')
    exchange_rate   = models.DecimalField('EXCHANGE RATE',  decimal_places=5,   max_digits=9,       default=1)
    comment         = models.CharField('COMMENT',           max_length=200,     blank=True,         null=True)
    cancel_note     = models.CharField('CANCEL NOTE',       max_length=200,     blank=True,         null=True)

    ''' Order status - normal life cycle. '''
    ordered         = models.BooleanField('ORDERED',            default=False)
    being_delivered = models.BooleanField('BEING DELIVERED',    default=False)
    received        = models.BooleanField('RECEIVED',           default=False)
    refund_request  = models.BooleanField('REFUND REQUESTED',   default=False)
    refund_granted  = models.BooleanField('REFUND GRANTED',     default=False)

    datetime_ordered    = models.DateTimeField('DATE ORDERED',      auto_now_add=True,  blank=True,     null=True)
    datetime_delivered  = models.DateTimeField('DATE DELIVERED',                        blank=True,     null=True)
    datetime_refund_req = models.DateTimeField('DATE REQUESTED',                        blank=True,     null=True)
    datetime_refund_res = models.DateTimeField('DATE RESPONSE',                         blank=True,     null=True)
    datetime_cancelled  = models.DateTimeField('DATE CANCELLED',                        blank=True,     null=True)

    class Meta:
        abstract = True


class PhoneFields(models.Model):

    phone1 = models.CharField('Phone 1', max_length=30, unique=True, blank=False, null=False)
    phone2 = models.CharField('Phone 2', max_length=30, unique=True, blank=True,  null=True)
    phone3 = models.CharField('Phone 3', max_length=30, unique=True, blank=True,  null=True)
    phone4 = models.CharField('Phone 4', max_length=30, unique=True, blank=True,  null=True)

    class Meta:
        abstract = True


class ProductStockFields(models.Model):

    qty_stock       = models.PositiveSmallIntegerField('FULL STOCK',
                                                validators=[MaxValueValidator(999)],    default=0, blank=True, null=True)
    qty_sold        = models.PositiveSmallIntegerField('QUANTITY SOLD',
                                                validators=[MaxValueValidator(999)],    default=0, blank=True, null=True)
    qty_color       = models.PositiveSmallIntegerField('QUANTITY BY COLOR',
                                                validators=[MaxValueValidator(999)],    default=0, blank=True, null=True)
    qty_size        = models.PositiveSmallIntegerField('QUANTITY BY SIZE',
                                                validators=[MaxValueValidator(999)],    default=0, blank=True, null=True)

    bool_in_stock   = models.BooleanField('IS IN STOCK',                                default=True)

    class Meta:
        abstract = True
