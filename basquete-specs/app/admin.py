from django.contrib import admin
from .models import *
from .forms import TimeForm, JogadorForm, PartidaForm, TreinadorForm, EstatisticaForm, TorneioForm

class JogadorInline(admin.TabularInline):
    model = Jogador
    form = JogadorForm
    extra = 1

class PartidaInline(admin.TabularInline):
    model = Partida
    form = PartidaForm
    extra = 1

class EstatisticaInline(admin.TabularInline):
    model = Estatistica
    form = EstatisticaForm
    extra = 1

class TimeAdmin(admin.ModelAdmin):
    inlines = [JogadorInline]
    form = TimeForm

class PartidaAdmin(admin.ModelAdmin):
    inlines = [EstatisticaInline]
    form = PartidaForm

class TreinadorAdmin(admin.ModelAdmin):
    form = TreinadorForm

class TorneioAdmin(admin.ModelAdmin):
    form = TorneioForm
    filter_horizontal = ['times']  # Facilita a seleção de times participantes

admin.site.register(Time, TimeAdmin)
admin.site.register(Jogador)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Treinador, TreinadorAdmin)
admin.site.register(Estatistica)
admin.site.register(Torneio, TorneioAdmin)
