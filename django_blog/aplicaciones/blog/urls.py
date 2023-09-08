from django.urls import path
from .views import home, generales, programacion, videojuegos, tecnologia, detalles_post 

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('<slug:slug>/', detalles_post, name='detalles_post'),
]
