from django.db import models

class Time(models.Model):
    nomeTime = models.CharField(max_length=150)
    cidadeTime = models.CharField(max_length=100)
    treinadorTime = models.ForeignKey('Treinador', on_delete=models.CASCADE, related_name='times')

    def __str__(self):
        return self.nomeTime


class Jogador(models.Model):
    nomeJogador = models.CharField(max_length=150)
    numeroCamisa = models.IntegerField()
    posicao = models.CharField(max_length=50)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    dataNascimento = models.DateField()
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogadores')

    def __str__(self):
        return f"{self.nomeJogador} - {self.time.nomeTime}"


class Treinador(models.Model):
    nomeTreinador = models.CharField(max_length=150)
    telefoneTreinador = models.CharField(max_length=11)
    dataNascimentoTreinador = models.DateField()

    def __str__(self):
        return self.nomeTreinador


class Partida(models.Model):
    timeCasa = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='partidas_casa')
    timeVisitante = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='partidas_visitante')
    dataPartida = models.DateField()
    localPartida = models.CharField(max_length=200)
    pontosCasa = models.IntegerField(default=0)
    pontosVisitante = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.timeCasa.nomeTime} vs {self.timeVisitante.nomeTime} - {self.dataPartida}"


class Estatistica(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='estatisticas')
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE, related_name='estatisticas')
    pontos = models.IntegerField(default=0)
    assistencias = models.IntegerField(default=0)
    rebotes = models.IntegerField(default=0)
    faltas = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.jogador.nomeJogador} - {self.partida}"


class Torneio(models.Model):
    nomeTorneio = models.CharField(max_length=100)
    descricaoTorneio = models.CharField(max_length=300)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    times = models.ManyToManyField(Time, related_name='torneios')

    def __str__(self):
        return self.nomeTorneio
