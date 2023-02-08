import pyttsx3
import helpers.datetimeHelper as datetimeHelper
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 100)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say('bolo seco')
engine.runAndWait()
res = datetimeHelper.currentDate()
print(res)
