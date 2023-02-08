import datetime


def currentDate():
    data = datetime.date.today().strftime('%d/%B/%Y')
    data = data.split('/')
    return data
