# ninjas
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Ninja(models.Model):
    nombre = models.CharField(max_length = 20)
    rango = models.CharField(max_length = 10)
    naturaleza = models.CharField(max_length = 20)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre

class Capitan(models.Model):
    nombre_capitan = models.CharField(max_length = 20)
    rango = models.CharField(max_length = 10)
    naturaleza = models.CharField(max_length = 20)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre_capitan

class EquipoNinja(models.Model):
    nombre_equipo = models.CharField(max_length = 30, default = "Nombre de Equipo")
    capitan = models.ForeignKey(Capitan, on_delete = models.CASCADE)
    integrantes = models.ManyToManyField(Ninja)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre_equipo

class Mision(models.Model):
    nombre_mision = models.CharField(max_length = 20)
    lugar = models.CharField(max_length = 20)
    rango = models.CharField(max_length = 1)
    equipo_encargado = models.ForeignKey(EquipoNinja, on_delete = models.CASCADE)
    status_mision = models.BooleanField()

    def __str__(self):
        return self.nombre_mision

class Registro_Examen(models.Model):
    equipo = models.ForeignKey(EquipoNinja, on_delete = models.CASCADE)
    aldea = models.CharField(max_length = 30, default = 'Aldea Konoha')
    numero_misiones = models.IntegerField()
    date = models.DateField()
    status_registro = models.BooleanField()

    # def __str__(self):
    #    return self.equipo

# Modelo de los productos del carrito de compras
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length = 100)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    image_url = models.CharField(max_length=100, blank=True)
    cantitad = models.IntegerField()

    def __str__(self):
        return self.nombre_producto


# Modelo para crear perfil de usuario registrado
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_name = models.CharField(max_length = 30, blank = True)
    user_last = models.CharField(max_length = 30, blank = True)
    email = models.EmailField(blank = True)
    bio = models.TextField(max_length = 500, blank = True)
    location = models.CharField(max_length = 30, blank = True)
    birth_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.user.username

# Buscar en models las diferentes instancias
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()


'''
Practica que sigue
Generar un modelo para los ninjas en misiones

Practica Que sigue de la que sigue
Cada equipo tiene un capitan y cada capitan tienne 3 personas mas.
EL capitan debe escoger a los 3 integrantes
'''

'''
Clase Lunes 26 de Febreo

Generar Formulario (Ya sea con createview o listview)

views.py
class Ninjutsu(CreateView):
    template_name = 'principal/ninjutsu.html'
    model = Jutsu_ninja
    fields = "__all__"
    success_url = reverse_lazy('reporte_arte_ninja_view') <---Redirecciona a este view

en forms.py
from .models import Jutsu_ninja
class Jutsu_ninja_form(forms.ModelForm):

    class Meta:
        model = Jutus_ninja
        fields = "__all__"

En el urls.py
.as_view()

Investigar <slug>

ModelForm
https://elbauldelprogramador.com/crear-formularios-en-django-partir-de-un-modelo-con-modelform/
'''
