from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from mainapp.views import index, products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('products/', include('mainapp.urls', namespace = 'products')),
    path('auth/', include('authapp.urls', namespace = 'auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
