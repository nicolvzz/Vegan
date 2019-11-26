from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_lista, name='post_lista'),
]