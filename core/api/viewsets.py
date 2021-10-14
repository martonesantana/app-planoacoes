from django.db.models.query import Prefetch
from rest_framework import viewsets
from core.api import serializers
from core import models
from rest_framework.permissions import IsAuthenticated


class SituacaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SituacaoSerializer
    queryset = models.Situacao.objects.all()


class CausaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CausaSerializer
    queryset = models.Causa.objects.all()


class AcaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.AcaoSerializer
    queryset = models.Acao.objects.all()


class DetalheAcaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.DetalheAcaoSerializer
    queryset = models.DetalheAcao.objects.all()

