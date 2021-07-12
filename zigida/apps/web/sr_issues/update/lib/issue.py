from django.db.models                               import Q

from zigida.common                                  import issue    as issue_common
from zigida.common                                  import user     as user_common
from zigida.apps.db.sr_issues.models                import SRIssue


def get_issue(i):

    issue = SRIssue.objects \
        .filter(
            Q(code = i['code'])
        ) \
        .exclude(
            Q(bool_deleted = True)
        ) \
        .values(
            'uuid_code', 'token_key', 'code', 'assigned_to_id', 'assigned_by_id', 'title', 'description', 'dev_note',
            'language', 'type', 'status', 'datetime_created', 'datetime_updated',  'last_updated_by', 'bool_deleted',

            'assigned_to', 'assigned_by',
            'assigned_to__fullname', 'assigned_to__email',
            'assigned_by__fullname', 'assigned_by__email',
        ).first()

    return issue


def update_issue(i, staff):

    issue = issue_common.get_issue(i)

    i['updated']       = False
    i['prev_status']   = issue.get_status_display()
    i['prev_type']     = issue.get_type_display()
    i['prev_assignee'] = (issue.assigned_to.fullname).title()

    if staff['assigner']:
        issue.assigned_to_id    = i['assigned_to']
        issue.title             = i['title']
        issue.description       = i['description']
        issue.type              = int(i['type'])

    if staff['assigner'] or str(i['assigned_to']) == str((i['user']).uuid_code):
        issue.dev_note          = i['dev_note']
        issue.language          = i['language']
        issue.status            = int(i['status'])
        issue.last_updated_by   = i['user_fullname']

        issue.save()

        i['updated'] = True

    i['curr_status']   = issue.get_status_display()
    i['curr_type']     = issue.get_type_display()
    i['curr_assignee'] = (issue.assigned_to.fullname).title()

    return issue, i
