from django import forms
from .models import EquipoNinja
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EquipoNinjaForm(forms.ModelForm):
    class Meta:
        model = EquipoNinja
        fields = '__all__'

# Formulario para Signup
class SignupForm(UserCreationForm):
    birth_date = forms.DateField(help_text = 'Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = '__all__'
