from django import forms

from teams.models import Teams, TeamTodos, Members


class TeamCreationForm(forms.ModelForm):

    class Meta:
        model = Teams
        fields = ['name', 'team_type']