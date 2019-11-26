from django.urls import path
from . import views

urlpatterns = [
    path('publicaciones', views.post_lista, name='post_lista'),
    path('', views.inicio, name='inicio'),
    path('productos', views.productos, name='productos')
]
