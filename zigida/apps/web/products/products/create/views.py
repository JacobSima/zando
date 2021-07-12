from django.contrib.auth.mixins                     import LoginRequiredMixin
from django.shortcuts                               import render
from django.views                                   import View

from zigida.common                                  import user as user_common
from zigida.core.user_level_mixins                  import UserLevelMixin
from .forms                                         import ProductCreateForm
from .input                                         import input_get_input


# Create your views here.
class ProductCreateView(LoginRequiredMixin, UserLevelMixin, View):
    login_url = '/login/'
    template_name, permission_needed = 'apps/products/create.html', 'SRB-MNG-3'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff  = user_common.check_allowed_staff(self)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        prod_create_form = ProductCreateForm

        context = {
            'i'         : i,
            'page_name' : ['management', 'product_create'],
            'staff'     : staff,
            'form'      : prod_create_form,
            # 'country'       : ip_data.get('country'),
        }

        return render(request, self.template_name, context)
