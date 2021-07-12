from django.db.models                                   import Q

from zigida.apps.db.sr_issues.models                    import SRIssue


def get_issues(i, staff):

    issues = SRIssue.objects\
        .exclude(
            Q(bool_deleted = True)
        ) \
        .values(
            'uuid_code', 'token_key', 'code', 'assigned_to_id', 'assigned_by_id', 'title', 'description', 'dev_note',
            'language', 'type', 'status', 'datetime_created', 'datetime_updated',  'last_updated_by', 'bool_deleted',

            'assigned_to__fullname', 'assigned_to__email',
            'assigned_by__fullname', 'assigned_by__email',
        ).order_by('status')

    if i['assignee']:
        issues = issues\
            .filter(
                Q(assigned_to__fullname__icontains = i['assignee'])
            )

    if i['assigner']:
        issues = issues\
            .filter(
                Q(assigned_by__fullname__icontains = i['assigner'])
            )

    if i['type']:
        issues = issues\
            .filter(
                Q(type__icontains = i['type'])
            )

    if not staff['assigner']:
        issues = issues \
            .exclude(
                Q(status = 3)
            )

    return issues
