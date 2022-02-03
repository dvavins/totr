from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls


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
    path('', include(tf_urls)),
    path('accounts/', include('accounts.urls')),

]
