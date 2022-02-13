from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls


from core import views
from core.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    # path('api/', include('')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('security/', include(tf_urls)),
    path('account/', include('account.urls')),
    path('todos/', include('todos.urls')),
    path('tranx/', include('tranx.urls')),
    path('teams/', include('teams.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
