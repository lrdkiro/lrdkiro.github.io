from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html',{'posts': posts})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='General'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre='General')
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'generales.html', {'posts': posts})

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Programacion'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre='Programacion')
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'programacion.html', {'posts': posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Videojuegos'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre='Videojuegos')
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'videojuegos.html', {'posts': posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Tecnologia'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre='Tecnologia')
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'tecnologia.html', {'posts': posts})

def detalles_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detalles_post': post})