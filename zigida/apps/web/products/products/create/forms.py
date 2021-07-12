from crispy_forms.helper                                import FormHelper

from django                                             import forms
from django.db.models                                   import Q

from zigida.apps.db.products.categories.models          import Category
from zigida.apps.db.products.colors.models              import Color
from zigida.apps.db.products.sizes.models               import Size
from zigida.apps.db.stores.stores.models                import Store


CATEG_CHOICES = Category.objects.exclude(Q(bool_deleted = True)).values_list('code', 'title')
COLOR_CHOICES = Color.objects.exclude(Q(bool_deleted    = True)).values_list('code', 'title')
SIZE_CHOICES  = Size.objects.exclude(Q(bool_deleted     = True)).values_list('code', 'title')
STORE_CHOICES = Store.objects.exclude(Q(bool_deleted    = True)).values_list('code', 'name')
print()

class ProductCreateForm(forms.Form):

    ititle          = forms.CharField(label='Product Title', widget=forms.TextInput(attrs={"title" : "Product Title"}), required=True)
    iimage          = forms.ImageField(label='Image', required=False)
    istores         = forms.ChoiceField(label='', widget=forms.RadioSelect(), choices=STORE_CHOICES)
    idescription    = forms.CharField(label='Description', widget=forms.Textarea(attrs={"row" : "3"}),required=True)
    iinfo           = forms.CharField(label='Information', widget=forms.Textarea(attrs={"row" : "3"}),required=True)
    iprice          = forms.CharField(label="Price", widget=forms.TextInput(attrs={'class': 'small-input number', 'pattern': '[0-9]+'}),required=False)
    idiscount_price = forms.CharField(label="Discount Price", widget=forms.TextInput(attrs={'class': 'small-input number', 'pattern': '[0-9]+'}),required=False)
    ilabel          = forms.CharField(label='Product Label', widget=forms.TextInput(attrs={"title" : "Product Label"}), required=False)
    icategory       = forms.ChoiceField(label='', widget=forms.RadioSelect(), choices=STORE_CHOICES)
    icolor          = forms.ChoiceField(label='', widget=forms.RadioSelect(), choices=STORE_CHOICES)
    isize           = forms.ChoiceField(label='', widget=forms.RadioSelect(), choices=STORE_CHOICES)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['pax'].choices = kwargs['initial']['names']
    #     # self.fields['pax'].widget  = forms.CheckboxSelectMultiple()
    #     self.helper = FormHelper()
