from django.urls import path
from Burger.views import Index

urlpatterns = [
    path('', Index),
];