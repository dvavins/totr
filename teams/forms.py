from django import forms

from account.models import Contact
from teams.models import Teams, Members, TranxGroup, TodosGroup


class TeamCreationForm(forms.ModelForm):

    class Meta:
        model = Teams
        fields = ['team', 'team_type']

    def __init__(self, *args, **kwargs):
        super(TeamCreationForm, self).__init__(*args, **kwargs)
        self.fields['team_type'].widget.attrs['class'] = 'dropdown-item'
        self.fields['team'].widget.attrs['required'] = 'true'


class MembersAddForm(forms.ModelForm):

    member = forms.ModelChoiceField(queryset=Contact.objects.filter())

    class Meta:
        model = Members
        fields = ['members']
    #
    #     if user:
    #         queryset = Contact.objects.filter(user=user)





