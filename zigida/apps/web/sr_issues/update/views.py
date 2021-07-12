from django.contrib                                     import messages
from django.contrib.auth.mixins                         import LoginRequiredMixin
from django.shortcuts                                   import render, redirect
from django.urls                                        import reverse_lazy
from django.views.generic                               import View

from zigida.core.user_level_mixins                      import UserLevelMixin
from zigida.common                                      import user  as user_common
from zigida.common.email                                import SRIssueNotificationEmail
from .forms                                             import IssueUpdateForm
from .lib                                               import issue as issue_lib
from zigida.apps.web.sr_issues.update.input             import input_get_input, input_post_input


# Create your views here.
class IssueUpdateView(LoginRequiredMixin, UserLevelMixin, View):
    login_url = '/login/'
    template_name, permission_needed = 'apps/sr_issues/issues.html', 'BTK-ITD-1'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff = user_common.check_allowed_staff(self)

        issue = issue_lib.get_issue(i)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        form = IssueUpdateForm(request.POST or None, instance=issue, staff=staff)

        context = {
            'i'         : i,
            'page_name' : 'issues',
            'action'    : 'update',
            'staff'     : staff,
            'form'      : form,
            'issue_code': issue['code'],
            # 'country'       : ip_data.get('country'),
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):

        i = input_post_input(self)

        staff = user_common.check_allowed_staff(self)

        # form = IssueUpdateForm(request.POST or None)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        issue, i = issue_lib.update_issue(i, staff)

        if issue:

            if i['updated']:
                SRIssueNotificationEmail(issue, ip_data, i=i).start()

            messages.success(request, "Issue successfully updated.")

            return redirect(reverse_lazy('web:issues:list') + '')

        messages.warning(request, "Issue not updated. Please try again.")

        context = {
            'i'         : i,
            'page_name' : 'issues',
            'action'    : 'update',
            'staff'     : staff,
            # 'form'      : form,
            'issue_code': issue['code'],
            # 'country' : ip_data.get('country'),
        }

        return redirect(self.request.META['HTTP_REFERER'])
