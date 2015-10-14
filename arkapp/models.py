from django.db import models
from datetime import datetime
from sorl.thumbnail import ImageField
#BAJAR LA VERSION pip install sorl-thumbnail==11.12.1b

# Create your models here.

class publicaciones(models.Model):
    id = models.AutoField(primary_key = True)
    usuarios = models.ForeignKey('usuarios')
    path = models.TextField(max_length = 2000)
    nombre = models.TextField(max_length = 512)
    descripcion = models.TextField(max_length = 1000)
    categorias = models.ForeignKey('categorias')
    subCategorias = models.ForeignKey('subCategorias')
    fechaSubida = models.DateField(auto_now = True)
    palabrasClave = models.TextField(max_length = 1000)
    visitas = models.IntegerField()
    objetoUID = models.TextField(max_length = 512)
    flag = models.IntegerField()

class referencias(models.Model):
    id = models.AutoField(primary_key = True)
    publicaciones = models.ForeignKey('publicaciones')
    usuarios = models.ForeignKey('usuarios')
    titulo = models.TextField(max_length = 255)
    fechaSubida = models.DateField(auto_now = True)
    palabrasClave = models.TextField(max_length = 1000)
    texto = models.TextField(max_length = 7900)
    objetoUID = models.TextField(max_length = 512)
    flag = models.IntegerField()

class valoraciones(models.Model):
    id = models.AutoField(primary_key = True)
    objetoUID = models.TextField(max_length = 128, primary_key = True)
    usuarios = models.ForeignKey('usuarios')
    valoracion = models.IntegerField()

class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombreUsuario = models.TextField(max_length = 128, unique = True)
    contrasena = models.TextField(max_length = 128)
    email = models.EmailField(max_length = 128, unique = True)
    foto = ImageField(upload_to='foto_usuario')
    fechaAlta = models.DateField(auto_now = True)
    flag = models.IntegerField()

class usuariosComplementos(models.Model):
    id = models.AutoField(primary_key=True)
    atributo = models.TextField(max_length = 100)
    valor = models.TextField(max_length = 100)
    flagPublico = models.IntegerField()

class categorias(models.Model):
	 id = models.AutoField(primary_key=True)
	 nombre = models.TextField(max_length = 512)

class subCategorias(models.Model):
	 id = models.AutoField(primary_key=True)
	 categorias = models.ForeignKey('categorias')
	 nombre = models.TextField(max_length = 512)
