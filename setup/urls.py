from django.contrib import admin
from django.urls import path, include
from Burger.views import Cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Burger.urls')),
    path('login', Cadastro, name="Cadastro")
]
