import re
from threading                                                      import Thread

from django.conf                                                    import settings
from django.core.mail                                               import send_mail
from django.db.models                                               import Q
from django.template.loader                                         import render_to_string
from django.utils.html                                              import strip_tags

from zigida.common                                                  import location as location_lib
from zigida.apps.db.communications.emails.models                    import Email
from zigida.common.user import get_user

platform    = settings.PLATFORM
IS_ENV      = settings.IS_ENV


def create_email_record(issue, sender, receiver, **kwargs):

    i        = kwargs.get('i')
    subject  = kwargs.get('subject')
    message  = kwargs.get('message')
    ip_data  = kwargs.get('ip_data')
    language = kwargs.get('language')

    if not message:
        message = i.get('message')
    if not subject:
        subject = i.get('subject')

    message.rstrip('\n')
    message = re.sub('\n+', ' ', message)
    message = re.sub(' +', ' ', message)

    # count = get_email_count(user, receiver)

    user_id     = None
    location_id = None

    if ip_data:
        fullname    = ip_data.get('ip')

    location_first  = location_lib.get_locations(None, ip_data=ip_data)

    if location_first:
        location_id = location_first.uuid_code

    user_id  = issue.assigned_to.uuid_code
    fullname = issue.assigned_by.fullname

    email                   = Email()

    email.user_id         = user_id
    email.location_id       = location_id

    email.sender            = sender
    email.receiver          = receiver
    email.subject           = subject
    email.message           = message
    email.language          = language
    email.count             = 0
    email.last_updated_by   = fullname

    email.save()

    return


class SRIssueNotificationEmail(Thread):

    def __init__(self, issue, ip_data, i=None):
        super(SRIssueNotificationEmail, self).__init__()
        self.receiver = issue.assigned_to.email
        self.sender   = settings.EMAIL_ISSUE_SENDER
        self.password = settings.EMAIL_ISSUE_PASSWORD
        self.issue    = issue
        self.ip_data  = ip_data
        self.i        = i
        self.user     = self.i['user']
        self.subject  = 'ISSUES NOTIFICATIONS'
        Thread.__init__(self)

    def run(self):

        if self.i['operation'] == 'C':
            self.send_assignment_notification()

        if self.i['operation'] == 'U':
            self.send_status_update_notification()
        # self.create_email_record()

    def create_email_record(self):

        email = Email()

        email.user_id = self.user_id
        email.location_id = self.location_id

        email.sender = self.sender
        email.receiver = self.receiver
        email.subject = self.subject
        email.message = self.message
        email.language = self.language
        email.count = 0
        email.last_updated_by = self.fullname

        email.save()

        return

    def send_assignment_notification(self):

        self.name      = self.issue.assigned_to.fullname
        self.firstname = (self.name.split(' ')[0]).capitalize()
        self.assigner  = ((self.issue.assigned_by.fullname).split(' ')[0]).capitalize()

        self.msg = f"""
            
            Hi, {self.firstname}.
            
            {self.assigner} has assigned issue '{self.issue.code}' to you.
            Please go to issues page to for more info.
            https://zigida.sbn.systems/issues/update/{self.issue.code}
            
            Should you have any question, please contact the assigner ({self.assigner}).

            Thanks,
            Zigida Team,
            Email: {self.issue.assigned_by.email}
        """

        send_mail(
            f"WEB :: {self.subject}",
            f"{self.msg}",
            self.sender,
            [f'{self.receiver}', ],
            fail_silently = False,
            auth_user     = self.sender,
            auth_password = self.password
        )

        return

    def send_status_update_notification(self):

        self.name      = self.issue.assigned_to.fullname
        self.firstname = (self.name.split(' ')[0]).title()
        self.user_name = ((self.i['user_fullname']).split(' ')[0]).capitalize()
        self.assigner  = ((self.issue.assigned_by.fullname).split(' ')[0]).title()

        for email in [self.issue.assigned_to.email, self.issue.assigned_by.email]:
            recv_name     = self.assigner
            self.receiver = email

            if email == self.issue.assigned_to.email:
                recv_name     = self.firstname

            if email == self.issue.assigned_by.email:
                recv_name     = self.assigner

            self.msg = f"""
    
                Hi, {recv_name}.
    
                Issue '{self.issue.code}' has been updated - status or assignee.
                Please check the following whether they have changed.
                
                Previous status "{self.i['prev_status']}", current status "{self.i['curr_status']}".
                Previous assignee "{self.i['prev_assignee']}" to current assignee "{self.i['curr_assignee']}".
                Previous type "{self.i['prev_type']}" to current type "{self.i['curr_type']}" or description.
                
                Please go to issues page to for more info.
                
                https://zigida.sbn.systems/issues/update/{self.issue.code}
    
                Should you have any question, please contact the assigner ({self.assigner}).
    
                Thanks,
                Zigida Team,
                Email: {self.sender}
            """

            if email != self.user.email:
                send_mail(
                    f"WEB :: {self.subject}",
                    f"{self.msg}",
                    self.sender,
                    [f'{self.receiver}', ],
                    fail_silently = False,
                    auth_user     = self.sender,
                    auth_password = self.password
                )

        return
