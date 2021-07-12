from crispy_forms.helper                                import FormHelper

from django                                             import forms
from django.contrib.auth                                import get_user_model
from django.db.models                                   import Q

from zigida.common.global_choices                       import ISSUE_TYPE, LANGUAGES


User = get_user_model()

STATUS_TYPE = (
    ('', '---------'),
    (1, 'Assigned'),
    (2, 'Resolved'),
    (3, 'Closed'),
)

class IssueUpdateForm(forms.Form):

    title       = forms.CharField(label='Issue Title', widget=forms.TextInput(attrs={"title" : "Issue Title"}),required=True)
    assigned_to = forms.ModelChoiceField(label='Developer', queryset=User.objects.filter(Q(user_type=1)),required=False)
    # assigned_by = forms.ModelChoiceField(label='Assigner', queryset=User.objects.filter(Q(user_type=1)),required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={"row" : "3"}),required=True)
    dev_note    = forms.CharField(label="Developer's Note", widget=forms.Textarea(attrs={"row" : "3"}),required=False)
    # language    = forms.ChoiceField(label='Language', initial='FR', choices=LANGUAGES,      required=False)
    type        = forms.ChoiceField(label='Type', initial=1,    choices=ISSUE_TYPE,     required=False)
    status      = forms.ChoiceField(label='Status', initial='',   choices=STATUS_TYPE,    required=False)

    def __init__(self, *args, **kwargs):
        staff = kwargs.pop('staff')
        issue = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

        self.fields['title'].initial        = issue['title']
        self.fields['assigned_to'].initial  = issue['assigned_to']
        self.fields['description'].initial  = issue['description']
        self.fields['dev_note'].initial     = issue['dev_note']
        self.fields['type'].initial         = issue['type']
        self.fields['status'].initial       = issue['status']

        if not staff['assigner']:
            self.fields['title'].widget.attrs['readonly']       = True
            self.fields['title'].widget.attrs['disabled']       = True
            self.fields['assigned_to'].widget.attrs['readonly'] = True
            self.fields['assigned_to'].widget.attrs['disabled'] = True
            self.fields['description'].widget.attrs['readonly'] = True
            self.fields['description'].widget.attrs['disabled'] = True
            self.fields['dev_note'].initial                     = issue['dev_note']
            self.fields['type'].widget.attrs['readonly']        = True
            self.fields['type'].widget.attrs['disabled']        = True
            self.fields['status'].initial                       = issue['status']

        self.helper = FormHelper()
