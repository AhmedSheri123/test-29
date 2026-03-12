from django.urls import path

from . import views

urlpatterns = [
    path('', views.excorx, name='excorx'),
]
