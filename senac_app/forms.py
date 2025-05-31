from django import forms
from .models import Curso, UserProfile, Contato

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'imagem', 'preco']  # Campos do formulário

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [] # Apenas o campo de foto


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']