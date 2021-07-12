from django.urls                                        import path, include

from zigida.apps.web.sr_issues.create.views             import IssueCreateView
# from zigida.apps.web.sr_issues.delete.views             import IssueDeleteView
from zigida.apps.web.sr_issues.list.views               import IssueListView
from zigida.apps.web.sr_issues.update.views             import IssueUpdateView

app_name = 'issues'

urlpatterns = [

        path('create/',                 IssueCreateView.as_view(),                  name='create'),
        # path('delete/<code>',             IssueDeleteView.as_view(),                  name='delete'),
        path('list/',                   IssueListView.as_view(),                    name='list'),
        path('update/<code>',           IssueUpdateView.as_view(),                  name='update'),

    ]
