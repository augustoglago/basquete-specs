from django import forms
from .models import Time, Jogador, Partida, Treinador, Estatistica, Torneio

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = '__all__'


class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = '__all__'


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'


class TreinadorForm(forms.ModelForm):
    class Meta:
        model = Treinador
        fields = '__all__'


class EstatisticaForm(forms.ModelForm):
    class Meta:
        model = Estatistica
        fields = '__all__'


class TorneioForm(forms.ModelForm):
    class Meta:
        model = Torneio
        fields = '__all__'
