from django.shortcuts import render
from .models import Noticias,Galerias
from .forms import RegistroForm

# Create your views here.
def inicio(request):
    #select * from producto
    noticias = Noticias.objects.all()
    data = {"noticias": noticias}
    return render(request,'servicios/noticiasBootstrap.html', data)

def registro(request):
    data= {'form': RegistroForm()}
    if request.method =='POST':
        formulario= RegistroForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registrado correctamente"
        else:
            data["form"]=formulario
    return render(request,'servicios/registro.html', data)

def carrito(request):
    return render(request,'servicios/carrito.html')

def galeria(request):
    galeria = Galerias.objects.all()
    data = {"galerias": galeria}
    return render(request, 'servicios/Galeria.html', data)

def noticia1(request):
    return render(request, 'servicios/noticia1.html')

def noticia2(request):
    return render(request, 'servicios/noticia2.html')

def noticia3(request):
    return render(request, 'servicios/noticia3.html')

def recuperacioncontra(request):
    return render(request, 'servicios/recuperarcontraseña.html')