from django.shortcuts import render

from teams.models import Teams
from teams.forms import TeamCreationForm


def home(request):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            data = Teams()
            data.name = form.changed_data['name']
            data.team_type = form.changed_data['team_type']
            data.admin = request.user
            data.save()
    else:
        form = TeamCreationForm()

    return render(request, 'index.html', context={'form': form})
