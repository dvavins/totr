from django.shortcuts import render

from account.models import Profile


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def viewprofile(request, username):
    profile = Profile.objects.get(slug=username)
    context = {
        'profile': profile
    }
    return render(request, 'viewprofile.html', context)
