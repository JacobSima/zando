from django.db.models                               import Q

from zigida.apps.db.sr_issues.models                import SRIssue


def get_issue(i):

    issue = SRIssue.objects \
        .filter(
            Q(code = i['code'])
        ) \
        .exclude(
            Q(bool_deleted = True)
        ) \
        .first()

    return issue
