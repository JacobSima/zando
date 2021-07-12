from django.shortcuts                                   import render
from django.views.generic                               import View

from zigida.common                                      import user as user_common
from zigida.apps.web.sr_users.forms                     import UserRegisterForm, UserLoginForm
from .input                                             import input_get_input


# Create your views here.
class ProductMenListView(View):
    template_name = 'apps/products/mens.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff = user_common.check_allowed_staff(self)
        
        login_form    = UserLoginForm
        register_form = UserRegisterForm

        META_INFO = request.META
    
        ip_data = META_INFO.get('ip_data')

        context = {
            'i'              : i,
            'page_name'      : 'products' or 'mens',
            'staff'          : staff,
            'login_form'     : login_form,
            'register_form'  : register_form,
            # 'country'      : ip_data.get('country'),
        }

        return render(request, self.template_name, context)


class ProductWomenListView(View):
    template_name = 'apps/products/womens.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff = user_common.check_allowed_staff(self)

        login_form    = UserLoginForm
        register_form = UserRegisterForm

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        context = {
            'i'             : i,
            'page_name'     : 'products' or 'womens',
            'staff'         : staff,
            'login_form'    : login_form,
            'register_form' : register_form,
            # 'country'      : ip_data.get('country'),
        }

        return render(request, self.template_name, context)
