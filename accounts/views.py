from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from accounts.forms import UserRegistrationForm


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password1,
            )
            user.save()
            return redirect('/accounts/signin/')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('/accounts/dashboard/')
    else:
        messages.error(request, 'Invalid user credentials')
    return render(request, 'accounts/signin.html')



def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'User have been successfully logged out.')
        return redirect('/accounts/signin')
    else:
        return redirect('/accounts/signin')



@login_required()
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


