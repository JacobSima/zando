from zigida.apps.db.sr_issues.models                        import SRIssue


def create_issue(i, staff):

    issue = SRIssue()

    issue.title             = i['title']
    issue.description       = i['description']
    issue.dev_note          = i['dev_note']
    issue.language          = i['language']
    issue.type              = i['type']
    issue.status            = i['status']
    issue.last_updated_by   = i['user_fullname']

    if staff['assigner']:
        issue.assigned_to_id = i['assigned_to']
        issue.assigned_by    = i['user']
    else:
        if str(i['assigned_to']) != str((i['user']).uuid_code):
            issue.assigned_to_id = i['assigned_to']
            issue.assigned_by_id = str((i['user']).uuid_code)

    issue.save()

    return issue
