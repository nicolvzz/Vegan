from django.urls import path
from . import views

urlpatterns = [
    path('publicaciones', views.post_lista, name='post_lista'),
    path('', views.inicio, name='inicio'),
    path('productos', views.productos, name='productos'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('post/nuevo', views.nuevo_post, name='nuevo_post'),
    path('post/<int:pk>/edit/', views.editar_post, name='editar_post'),
    path('EliminarPost/<int:pk>/', views.eliminar_post, name='eliminar_post'),
    path('logout', views.logout),
     path('login', views.login, name='login'),

]
