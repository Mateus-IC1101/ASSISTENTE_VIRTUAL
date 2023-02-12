import data.respostas as __REPOSITORY_RESPOSTAS__
import pyttsx3
import helpers.datetimeHelper as datetimeHelper
from gtts import gTTS
import subprocess as s
import webbrowser
# import tensorflow as tf
# Teste
# print(__REPOSITORY_RESPOSTAS__.EMOCOES)
#
# ----------------------------------- voz api google-----------------------------

voz = gTTS('Você não tem eventos para hoje', lang="pt")
voz.save('voz.mp3')
s.call(['mplayer', 'voz.mp3'])

# ----------------------------------- voz api google-----------------------------

# ----------------------------------- voz pyttsx3 -----------------------------

engine = pyttsx3.init()
rate = engine.getProperty('rate')  # palavras por min
engine.setProperty('rate', 100)  # ajuste de palavras por min
voices = engine.getProperty('voices')  # vozes
volume = engine.getProperty('volume')  # volume atual
engine.setProperty('volume', volume - 0.1)  # ajuste de volume
# atribuindo índice de voz brasileira
engine.setProperty("voice", voices[59].id)
engine.say('Você não tem eventos para hoje')  # entrada de texto
engine.runAndWait()
engine.stop()
# ----------------------------------- voz pyttsx3 -----------------------------


# ----------------------------------- webbrowser -----------------------------
path = 'xdg-open google.com'
pesquisa = 'python'
webbrowser.open('https://www.google.com.br/search?q='+pesquisa)


# def loadModel(): # desativado temporariamente
#     model = tf.keras.models.load_model(
#         'models/speech_emotion_recognition.hdf5')
#     model_dict = sorted(list(['Feliz', 'Triste', 'Cansado']))
#     TAXA = 48000
#     return model, model_dict, TAXA


# print(loadModel()[0].summary())
