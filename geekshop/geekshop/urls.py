from django.contrib import admin
from django.urls import path, include
from mainapp import urls
from .views import contacts, main

app_name = 'geekshop'

urlpatterns = [
    path('', main, name='index'),
    path('admin/', admin.site.urls),
    path('products/', include(urls), name='products'),
    path('contacts/', contacts, name='contacts'),
]