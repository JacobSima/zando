from django.contrib.auth.mixins                         import LoginRequiredMixin
from django.shortcuts                                   import render
from django.views.generic                               import View

from zigida.core.user_level_mixins                      import UserLevelMixin
from zigida.common                                      import user  as user_common
from ..create.forms                                     import IssueCreateForm
from zigida.apps.web.sr_issues.list.input               import input_get_input
from .lib                                               import issue as issue_lib


# Create your views here.
class IssueListView(LoginRequiredMixin, UserLevelMixin, View):
    login_url = '/login/'
    template_name, permission_needed = 'apps/sr_issues/issues.html', 'BTK-ITD-1'

    def get(self, request, **kwargs):

        i = input_get_input(self)

        staff  = user_common.check_allowed_staff(self)

        issues = issue_lib.get_issues(i, staff)

        META_INFO = request.META

        ip_data = META_INFO.get('ip_data')

        form = IssueCreateForm

        context = {
            'i'         : i,
            'page_name' : 'issues',
            'issues'    : issues,
            'staff'     : staff,
            'form'      : form,
            # 'country'       : ip_data.get('country'),
        }

        return render(request, self.template_name, context)
