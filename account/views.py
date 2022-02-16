import qrcode
import qrcode.image.svg
from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from account.models import Account, Contact, Referral
from account.forms import UserRegistrationForm, SigninForm


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
            return redirect('/account/signin/')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)


# def signin(request):
#     if request.method == 'POST':
#         form = SigninForm(request.POST)
#
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 messages.success(request, 'Login Successfully')
#                 return redirect('/account/dashboard/')
#     else:
#         print('error')
#         form = SigninForm
#         messages.error(request, 'Invalid user credentials')
#     context = {
#         'form': form
#     }
#     return render(request, 'account/signin.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'User have been successfully logged out.')
        return redirect('/account/login')
    else:
        return redirect('/account/login')


@login_required(login_url='account:signin')
def dashboard(request):
    return render(request, 'account/dashboard.html')


def profile(request):
    pass


@login_required(login_url='two_factor:login')
def refer(request):
    data = Referral()
    svg = None
    try:
        if request.user.is_authenticated:
            ref = Referral.objects.get(user=request.user, is_used=False)
            factory = qrcode.image.svg.SvgImage
            if ref:
                img = qrcode.make(ref.ref_code, image_factory=factory, box_size=20)
            else:
                data.objects.create(user= request.user)
                ref = Referral.objects.get(user=request.user, is_used=False)
                img = qrcode.make(ref.ref_code, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            svg = stream.getvalue().decode()
            print(svg)
    except:
        pass
    context = {
        'img': svg
    }
    return render(request, 'account/refer.html', context)


def viewproile(request, usernm):
    pass


