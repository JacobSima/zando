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

class IssueCreateForm(forms.Form):

    title       = forms.CharField(label='Issue Title', widget=forms.TextInput(attrs={"title" : "Issue Title"}),required=True)
    assigned_to = forms.ModelChoiceField(label='Developer', queryset=User.objects.filter(Q(user_type=1)),required=False)
    # assigned_by = forms.ModelChoiceField(label='Assigner', queryset=User.objects.filter(Q(user_type=1)),required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={"row" : "3"}),required=True)
    dev_note    = forms.CharField(label="Developer's Note", widget=forms.Textarea(attrs={"row" : "3"}),required=False)
    # language    = forms.ChoiceField(label='Language', initial='FR', choices=LANGUAGES,      required=False)
    type        = forms.ChoiceField(label='Type', initial=1,    choices=ISSUE_TYPE,     required=False)
    status      = forms.ChoiceField(label='Status', initial='',   choices=STATUS_TYPE,    required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.fields['pax'].choices = kwargs['initial']['names']
    #     # self.fields['pax'].widget  = forms.CheckboxSelectMultiple()
    #     self.helper = FormHelper()
