from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

# Create your models here.


class Situacao(models.Model):
    data = models.DateField('Data')
    periodo = models.DateField('Período')
    situacao = models.CharField('Situação', max_length=100)
    valor = models.DecimalField('Valor', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'

    def __str__(self):
        return self.situacao


class Causa(models.Model):
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE, related_name='situacoes')
    causas = models.CharField('Causas', max_length=100)
    valor = models.DecimalField('Valor', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'

    def __str__(self):
        return self.causas


class Acao(models.Model):
    causas = models.ForeignKey(Causa, on_delete=models.CASCADE, related_name='detcausas')
    acao = models.CharField('Ação', max_length=100)
    valor = models.DecimalField('Valor', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):
        return self.acao

class DetalheAcao(models.Model):
    STATUS_CHOICES = {
        ('Andamento','Andamento'),
        ('Concluído','Concluído'),
        }
    acao = models.ForeignKey(Acao, on_delete=CASCADE, related_name='acoes')
    detalhe = models.CharField('Detalhes', max_length=100)
    data = models.DateField('Data')
    status = models.CharField('Status', max_length = 100, choices=STATUS_CHOICES, default='Andamento')
    valor = models.DecimalField('Valor', max_digits=20, decimal_places=2,default=0)

    class Meta:
        verbose_name = 'Detalhes da Ação'
        verbose_name_plural = 'Detalhes das Ações'

    def __str__(self):
        return self.detalhe