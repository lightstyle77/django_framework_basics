from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainapp import urls
from . import settings
from .views import contacts, main

app_name = 'geekshop'

urlpatterns = [
    path('', main, name='index'),
    path('admin/', admin.site.urls),
    path('products/', include(urls), name='products'),
    path('contacts/', contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)