from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def post_lista(request):
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'vegan/post_lista.html', {'posts': posts})
def inicio(request):
    return render(request, 'vegan/inicio.html',{})
    
def productos(request):
    return render(request, 'vegan/productos.html',{})
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'vegan/detalle_post.html', {'post': post})