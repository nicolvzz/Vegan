from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

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
def nuevo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'vegan/editar_post.html', {'form': form})


def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'vegan/editar_post.html', {'form': form})