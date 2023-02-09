import datetime

# -------------- BRASIL --------------


def currentDateAndTimeBrasil():
    data = datetime.datetime.now()
    hora = datetime.datetime.time(data).hour
    minuto = datetime.datetime.time(data).minute
    return {'data': data.strftime('%d/%B/%Y'), 'hora': hora, 'minuto': minuto}


def currentDateSplitBrasil():
    data = datetime.date.today().strftime('%d/%B/%Y')
    data = data.split('/')
    return data


def currentTime():
    hora = datetime.datetime.now().strftime('%H:%M')
    return hora


# -------------- AMERICA --------------
def currentDateAmerica():
    data = datetime.date.today()
    return data
