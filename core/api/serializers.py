from rest_framework import fields, serializers
from core import models


class DetalheAcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetalheAcao
        fields = '__all__'

class AcaoSerializer(serializers.ModelSerializer):
    acoes=DetalheAcaoSerializer(read_only=True, many=True)
    class Meta:
        model = models.Acao
        fields = '__all__'

class CausaSerializer(serializers.ModelSerializer):
    detcausas = AcaoSerializer(read_only=True, many=True)
    class Meta:
        model = models.Causa
        fields = '__all__'

class SituacaoSerializer(serializers.ModelSerializer):
    situacoes = CausaSerializer(read_only=True, many=True)
    class Meta:
        model = models.Situacao
        fields = '__all__'
