from rest_framework import fields, serializers
from core import models


class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Situacao
        fields = '__all__'


class CausaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Causa
        fields = '__all__'


class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acao
        fields = '__all__'


class DetalheAcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetalheAcao
        fields = '__all__'
