from threading import Thread

from django.contrib                                     import messages
from django.contrib.auth                                import login, logout
from django.shortcuts                                   import render, redirect
from django.urls                                        import reverse_lazy
from django.views.generic                               import View

from zigida.common                                      import user  as user_common
from zigida.apps.web.sr_users.forms                     import UserRegisterForm, UserLoginForm
from zigida.apps.web.sr_users.input                     import input_get_input, input_post_input


# Create your views here.
class UserRegisterView(View):
    template_name = 'apps/home/index.html'
    # template_email = 'apps/home/confirmation_email.html'

    def post(self, request, **kwargs):

        i = input_post_input(self)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        form = UserRegisterForm(request.POST or None)

        # app_name = 'User'
        # action   = 'register'

        i['location_id'] = None

        if form.is_valid():
            new_sr_user = form.save(commit=False)

            new_sr_user.username  = new_sr_user.email
            new_sr_user.is_active = True

            new_sr_user.save()

            # Thread(target=sr_user_lib.sr_user_updates, args=(self, i, ip_data, new_sr_user)).start()
            #
            # host = request.META['HTTP_HOST']
            # link = f"{ip_data['pre_host']}://{host}/en/email/{new_sr_user.token_key}/{new_sr_user.code}/"
            #
            # email_context = {
            #     'link'          : link,
            #     'sr_user_name'   : new_sr_user.fullname,
            #     'template_email': self.template_email,
            # }
            #
            # SendEmail(new_sr_user, context = email_context, lang='EN', ip_data=ip_data).start()

            # audit_process.build_audit_dict(i, app_name, action, remote_ip=ip_data.get('ip'), item_pk=item_pk)

            messages.success(request, "We have sent you an email with ZIGIDA account activation instructions.")

            return redirect(self.request.META['HTTP_REFERER'])

            # return redirect(reverse_lazy('system:views:en:login') + '')

        messages.warning(request, "Oops! Something went wrong. Please try again.")

        context = {
            'i'             : i,
            'page_name'     : 'home',
            'register_form' : form,
        }

        return redirect(reverse_lazy('web:home') + '')


class UserLoginView(View):
    template_name = 'apps/home/index.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff = user_common.check_allowed_staff(self)

        login_form    = UserLoginForm
        register_form = UserRegisterForm

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        country = 'CD'

        if ip_data:
            country = ip_data.get('country')

        context = {
            'i'             : i,
            'page_name'     : 'home',
            'staff'         : staff,
            'login_form'    : login_form,
            'register_form' : register_form,
            'country'       : country#ip_data.get('country'),
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        i = input_post_input(self)

        form = UserLoginForm(request.POST or None)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        if form.is_valid():

            user_obj = form.cleaned_data.get('user_obj')

            login(request, user_obj)

            # phone_number = ""
            # sms = SendSMS(phone_number, message=None, otp=None)
            # sms.send_english()

            # messages.success(request, "Welcome back to ZIGIDA platform.")

            if i.get('next'):

                return redirect(i['next'])

            return redirect(self.request.META['HTTP_REFERER'])
            # return redirect(reverse_lazy('system:views:en:dashboard') + '')

        messages.warning(request, "Please check your login credentials and try again.")

        context = {
            'i'             : i,
            'page_name'     : 'home',
            'login_form'    : form,
            # 'country'       : ip_data.get('country'),
        }

        return redirect(reverse_lazy('web:home') + '')


class UserLogoutView(View):
    template_name = 'apps/home/index.html'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        logout(request)

        return redirect(reverse_lazy('web:home') + '')
