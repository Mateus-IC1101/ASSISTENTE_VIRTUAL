from gtts import gTTS


def saveText():
    texto = str(input('Texto: '))
    voz = gTTS('Você guardou a sua preferência em aúdio, irei lê agora. ' +
               ' ' +
               ' ' +
               ' ' +
               texto, lang="pt")
    voz.save('voz.mp3')


saveText()
