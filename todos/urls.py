from django.urls import path

from todos import views

app_name = 'todos'

urlpatterns = [
    path('add/', views.addtodo, name='addtodo'),
    path('view/', views.viewtodos, name='viewtodos'),
    path('view/<slug:todo_name>/', views.tododetail, name='tododetail'),
    path('view/<slug:todo_name>/delete/', views.deletetodo, name='deletetodo'),
]