from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('Registro',views.registro, name='registro'),
    path('Servicios',views.carrito,name='carrito'),
    path('Galeria',views.galeria, name='galeria'),
    path('Noticia1',views.noticia1,name='noticia1'),
    path('Noticia2',views.noticia2,name='noticia2'),
    path('Noticia3',views.noticia3,name='noticia3'),
    path('recuContra',views.recuperacioncontra,name='recuContra'),
]