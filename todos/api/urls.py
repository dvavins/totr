from os import name
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.getRoutes, name='getroute'),
    path('view/', views.viewTodos, name='viewtodos'),
    path('view/<str:pk>', views.detailView, name='detailview'),
    path('view/<str:pk>/update', views.updateTodo, name='updatetodo'),
    path('view/<str:pk>/delete', views.deleteTodo, name='deletetodo'),
    path('create/', views.createTodo, name='createtodo'),



    path('team/create', views.createTeam, name='createteam')
]
