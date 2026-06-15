from django.db import models
from django.contrib.auth.models import AbstractUser
from setores.models import Setor

# Create your models here.
class Usuario(AbstractUser):
    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    setor = models.ForeignKey(
        Setor,
        on_delete=models.CASCADE
    )
    