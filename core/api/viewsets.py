from django.db.models.query import Prefetch
from rest_framework import viewsets
from core.api import serializers
from core import models
from rest_framework.permissions import IsAuthenticated


class SituacaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Situacao.objects.all()
    serializer_class = serializers.SituacaoSerializer


class CausaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Causa.objects.all()
    serializer_class = serializers.CausaSerializer


class AcaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Acao.objects.all()
    serializer_class = serializers.AcaoSerializer


class DetalheAcaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.DetalheAcao.objects.all()
    serializer_class = serializers.DetalheAcaoSerializer

