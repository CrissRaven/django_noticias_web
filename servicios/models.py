from django.db import models

# Create your models here.
class Servicios(models.Model):
    nombre =models.CharField(max_length=70)
    precio =models.IntegerField()

    def __str__(self):
        return self.nombre

class Registros(models.Model):
    usuario =models.CharField(max_length=50)
    correo =models.CharField(max_length=50)
    contra =models.CharField(max_length=40)
    Servicios =models.ForeignKey(Servicios, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario
    
class Noticias(models.Model):
    noticia = models.CharField(max_length=100)
    descrip = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.noticia
    
class Galerias(models.Model):
    nombre= models.CharField(max_length=100)
    galeria= models.ImageField(upload_to="galeria", null=True)

    def __str__(self):
        return self.nombre
        