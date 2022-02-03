from django.contrib import admin
from django.urls import path, include

from core import views
from core.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('api/', include('')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('todos/', include('todos.urls')),
    path('tranx/', include('tranx.urls')),
    path('accounts/', include('accounts.urls')),
]
