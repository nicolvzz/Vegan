from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def post_lista(request):
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'vegan/post_lista.html', {'posts': posts})