from django.contrib import admin

from core.models import Acao, Causa, DetalheAcao, Situacao

# Register your models here.
@admin.register(Situacao)
class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('situacao','data','periodo','valor')

@admin.register(Causa)
class CausaAdmin(admin.ModelAdmin):
    list_display = ('causas','situacao','valor')

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('acao', 'causas', 'valor')


@admin.register(DetalheAcao)
class DetalheAcaoAdmin(admin.ModelAdmin):
    list_display = ('detalhe', 'acao', 'data','status', 'valor')

