from django.contrib import admin
from .models import (Ninja, Capitan, EquipoNinja, Mision, Registro_Examen, Perfil,
Products)

# Register your models here.
admin.site.register(Ninja)
admin.site.register(Capitan)
admin.site.register(EquipoNinja)
admin.site.register(Mision)
admin.site.register(Registro_Examen)
admin.site.register(Perfil)
admin.site.register(Products)
