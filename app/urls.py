"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


from rest_framework import routers
from core.api import viewsets as situacaoviewsets

route = routers.DefaultRouter()

route.register(r'situacao', situacaoviewsets.SituacaoViewSet, basename="Situações")
route.register(r'causa', situacaoviewsets.CausaViewSet, basename="Causas")
route.register(r'acao', situacaoviewsets.AcaoViewSet, basename="Ações")
route.register(r'detalheacao', situacaoviewsets.DetalheAcaoViewSet, basename="DetalhesAções")


urlpatterns = [
    path('', RedirectView.as_view(url='/app/')),
    path('app/', admin.site.urls),
    path('api/', include(route.urls)),
       
]



