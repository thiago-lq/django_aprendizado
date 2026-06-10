from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Chamados(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    usuario = models.ForeignKey(
        Usuario,
        on_delete = models.CASCADE
    )

    class Setor(models.TextChoices):
        CONTABILIDADE = "CT", "CONTABILIDADE"
        SECRETARIA = "ST", "SECRETARIA"
        COMPRAS_FINANCEIRO = "CF", "COMPRAS E FINANCEIRO"
        COORDENACAO = "CO", "COORDENAÇÃO"
        REUNIAO_ANEXO = "RA", "REUNIÃO ANEXO"
        ANEXO = "AN", "ANEXO"
        TECNICOS = "TC", "TÉCNICOS"
        RECEPCAO = "RC", "RECEPÇÃO"
        OUTROS = "OT", "OUTROS"

    
    setor = models.CharField(
        max_length = 2,
        choices = Setor.choices,
        default = Setor.SECRETARIA
    )
    
    class Prioridade(models.TextChoices):
        ALTA = "AL", "ALTA"
        MEDIA = "ME", "MEDIA"
        BAIXA = "BA", "BAIXA"

    prioridade = models.CharField(
        max_length = 2,
        choices = Prioridade.choices,
        default = Prioridade.BAIXA,
    )

    data_hora= models.DateTimeField(auto_now_add = True)
    prazo = models.DateField()
