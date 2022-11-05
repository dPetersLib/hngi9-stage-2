from django.urls import path
from api.views import enum

urlpatterns = [
    path('', enum, name='enum')
]
