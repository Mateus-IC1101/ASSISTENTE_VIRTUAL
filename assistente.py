import data.respostas as __REPOSITORY_RESPOSTAS__
import pyttsx3
import helpers.datetimeHelper as datetimeHelper
import webbrowser
import tensorflow as tf
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[59].id)
engine.setProperty('rate', rate - 70)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume - 0.1)
engine.say('Você não tem eventos para hoje')

engine.runAndWait()
engine.stop()

path = 'xdg-open google.com'
webbrowser.open('https://www.python.org')


print(__REPOSITORY_RESPOSTAS__.EMOCOES)


def loadModel():
    model = tf.keras.models.load_model(
        'models/speech_emotion_recognition.hdf5')
    model_dict = sorted(list(['Feliz', 'Triste', 'Cansado']))
    TAXA = 48000
    return model, model_dict, TAXA


print(loadModel()[0].summary())
