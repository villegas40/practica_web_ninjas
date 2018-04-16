from django import forms
from .models import EquipoNinja, Perfil
from django.contrib.auth.forms import UserCreationForm # Registrar usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm # Para editar nuestro user

class EquipoNinjaForm(forms.ModelForm):
    class Meta:
        model = EquipoNinja
        fields = '__all__'

# Formulario para Signup
class SignupForm(UserCreationForm):
    # user = forms.CharField(max_length = 20, required = True, help_text = 'User name max lenght 30 characters.')
    #bio = formsself.CharField(max_length = 500,  )
    user_name = forms.CharField(max_length = 30, help_text = 'Enter first name, max 30 characters.')
    user_last = forms.CharField(max_length = 30, help_text = 'Enter last name, max 30 characters.')
    birth_date = forms.DateField(help_text = 'Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'user_name', 'user_last', 'birth_date', 'email' , 'password1', 'password2', )

class EditProfileForm(UserChangeForm):
    birth_date = forms.DateField(help_text = 'Required. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password')
