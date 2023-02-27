import speech_recognition as sr
import pocketsphinx

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
# import speech_recognition as sr
# rec = sr.Recognizer()

# with sr.Microphone() as fala:
#     frase = rec.listen(fala)
# print(rec.recognize_google(frase))
