from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import (
    consulta_times,
    consulta_jogadores,
    consulta_partidas,
    consulta_treinadores,
    consulta_estatisticas,
    consulta_torneios
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('consultaTimes/', consulta_times, name='consultaTimes'),
    path('consultaJogadores/', consulta_jogadores, name='consultaJogadores'),
    path('consultaPartidas/', consulta_partidas, name='consultaPartidas'),
    path('consultaTreinadores/', consulta_treinadores, name='consultaTreinadores'),
    path('consultaEstatisticas/', consulta_estatisticas, name='consultaEstatisticas'),
    path('consultaTorneios/', consulta_torneios, name='consultaTorneios'),
]
