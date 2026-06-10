from django import forms
from .models import Chamados

class ChamadoForm(forms.ModelForm):
    prazo = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Formato: AAAA-MM-DD"
    )

    class Meta:
        model = Chamados
        fields = ['titulo', 'descricao', 'setor', 'prioridade', 'prazo']
        labels = {
            'titulo': 'Título do Chamado', 
            'descricao': 'Descrição do chamado',
            'setor': 'Setor do problema',
            'prioridade': 'Nível de Prioridade',
            'prazo': 'Prazo para resolução'
        }

        widgets = {
            'titulo': forms.TextInput(attrs= {'class': 'form-input'}),
            'descricao': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5}),
            'setor': forms.Select(attrs={'class': 'form-select'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'})
        }