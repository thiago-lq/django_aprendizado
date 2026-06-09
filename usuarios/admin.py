from django.contrib import admin
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'setor')
    list_filter = ('nome', 'setor')
    search_fields = ('nome', 'cpf')