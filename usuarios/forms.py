from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'email', 'setor']
        labels = {
            'nome': 'Nome do Usuário',
            'cpf': 'CPF do Usuário',
            'email': 'Email do Usuário',
            'setor': 'Setor de trabalho'
        }

        widgets = {
            'nome': forms.TextInput(attrs = {'class': 'form-input'}),
            'cpf': forms.TextInput(attrs = {'class': 'form-input'}),
            'email': forms.EmailInput(attrs = {'class': 'form-email'}),
            'setor': forms.Select(attrs = {'class': 'form-select'})
        }
