from django.urls import path

from tranx import views

app_name = 'tranx'

urlpatterns = [
    path('add/', views.addtranx, name='addtranx'),
    path('view/', views.viewtranx, name='viewtranx'),
    path('view/<slug:tranx_name>/', views.detailtranx, name='detailtranx')
]