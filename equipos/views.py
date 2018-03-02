from django.shortcuts import render, redirect # Redirect singup
from .forms import EquipoNinjaForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate # singup up
from django.contrib.auth.forms import UserCreationForm # Importar para singup
from .forms import SignupForm # Formulario creado para el perfil

# Create your views here.
def equipo_view(request):
    if request.method == "POST":
        form = EquipoNinjaForm(request.POST)
        if form.is_valid():
            new_team = form.save()

            return HttpResponseRedirect('/equipo_edit/')
    else:
        form = EquipoNinjaForm()
    return render(request, 'equipos/equipo_edit.html', {'form':form})

# Creacion del signup
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            login(request, user)
            return redirect('/signup/')
    else:
        form = UserCreationForm()
    return render(request, 'equipos/signup.html', {'form':form})

def signup_user_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # Carga la instancia de perfil crada por signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('/equipo_edit/')

    else:
        form = SignupForm()
    return render(request, 'equipos/register.html', {'form': form})
