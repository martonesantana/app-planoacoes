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


class DetalheAcaoSerializer(serializers.ModelSerializer):
    acoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    
    class Meta:
        model = models.DetalheAcao
        fields = '__all__'

class AcaoSerializer(serializers.ModelSerializer):
    feeds = DetalheAcaoSerializer(many=True, read_only=True)
    class Meta:
        model = models.Acao
        fields = '__all__'