from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from two_factor.urls import urlpatterns as tf_urls


from core import views
from core.routers import router

urlpatterns = [
    path('mysite/admin/', admin.site.urls),

    # Home
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('profile/<str:username>/', views.viewprofile, name='viewprofile'),

    # Account (Authentication Required)
    path('', include(tf_urls)),
    path('account/', include('account.urls')),

    # Todos (Personal) (Authentication Required)
    path('todos/', include('todos.urls')),
    # Tranx (Personal) (Authentication Required)
    path('tranx/', include('tranx.urls')),
    # Teams (Authentication Required)
    path('teams/', include('teams.urls')),


    # Api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
