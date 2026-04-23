from .models import Autor, Libro
from django import forms

class AutorForm(forms.ModelForm):
    class Meta:
    model = Autor
    fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']