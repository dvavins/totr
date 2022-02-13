from os import name
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.getRoutes, name='getroute'),
    path('view/', views.viewAccounts, name='viewAccounts'),
    # path('view/<str:pk>', views.detailView, name='detailview'),
    # path('view/<str:pk>/update', views.updateAccount, name='updateAccount'),
    # path('view/<str:pk>/delete', views.deleteAccount, name='deleteaccount'),
    path('create/', views.createAccount, name='createAccount'),



    path('team/create', views.createTeam, name='createteam')
]
