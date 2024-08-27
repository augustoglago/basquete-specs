from django.shortcuts import render
from .models import *

def consulta_times(request):
    consultaTime = Time.objects.all()
    context = {'consultaTimes': consultaTime}
    return render(request, 'consulta/consultaTimes.html', context)

def consulta_jogadores(request):
    consultaJogador = Jogador.objects.all()
    context = {'consultaJogadores': consultaJogador}
    return render(request, 'consulta/consultaJogadores.html', context)

def consulta_partidas(request):
    consultaPartida = Partida.objects.all()
    context = {'consultaPartidas': consultaPartida}
    return render(request, 'consulta/consultaPartidas.html', context)

def consulta_treinadores(request):
    consultaTreinador = Treinador.objects.all()
    context = {'consultaTreinadores': consultaTreinador}
    return render(request, 'consulta/consultaTreinadores.html', context)

def consulta_estatisticas(request):
    consultaEstatistica = Estatistica.objects.all()
    context = {'consultaEstatisticas': consultaEstatistica}
    return render(request, 'consulta/consultaEstatisticas.html', context)

def consulta_torneios(request):
    consultaTorneio = Torneio.objects.all()
    context = {'consultaTorneios': consultaTorneio}
    return render(request, 'consulta/consultaTorneios.html', context)
