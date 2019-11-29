from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login

# Create your views here.

def post_lista(request):
    user = request.user
    if user.has_perm('vegan.lector'):
        posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
        return render(request, 'vegan/post_lista.html', {'posts': posts})
    elif user.has_perm('vegan.admin'):
        posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
        return render(request, 'vegan/post_lista.html', {'posts': posts})
    else:
        return redirect ('/login')
def inicio(request):
    return render(request, 'vegan/inicio.html',{})
    
def productos(request):
    return render(request, 'vegan/productos.html',{})
def detalle_post(request, pk):
    user = request.user
    if user.has_perm('vegan.admin'):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'vegan/detalle_post.html', {'post': post})
    else:
        posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
        return render(request, 'vegan/post_lista.html', {'posts': posts})


def nuevo_post(request):
    user = request.user
    if user.has_perm('vegan.admin'):
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
    else:
        posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
        return render(request, 'vegan/post_lista.html', {'posts': posts})


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

def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_lista')

def logout(request):
    do_logout(request)
    return redirect('login')
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "vegan/login.html", {'form': form})

    