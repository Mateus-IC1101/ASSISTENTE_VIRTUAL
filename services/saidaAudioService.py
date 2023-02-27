# -----voz api google
import subprocess as s
# -----voz api google


def executarTeste():
    s.call(['mplayer', './voz.mp3'])


def executarAlarme():
    s.call(['mplayer', '../storage/audios/alarme/alarm-clock-short.mp3'])


def executarVozAlarme():
    s.call(['mplayer', '../storage/audios/vozAlarme/bom_dia.mp3'])


executarTeste()
# executarVozAlarme()
# executarAlarme()
