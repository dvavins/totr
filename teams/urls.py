from django.urls import path

from teams import views

app_name = 'teams'

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.addmember, name='addmember'),
]