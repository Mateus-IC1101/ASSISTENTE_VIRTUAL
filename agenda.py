import pandas as pd
import datetime
import helpers.datetimeHelper as datetimeHelper
from pandas_ods_reader import read_ods

'''

!INFORMAÇÕES DOC!
No excel, a data precisa ser brasileira: 08/02/2023

'''

df = pd.read_excel('agenda.ods')
data_atual = datetimeHelper.currentDateAmerica()
for index, row in df.iterrows():
    data = datetime.datetime.date(row['data'])
    hora_extraida = datetime.datetime.strptime(str(row['hora']), '%H:%M:%S')
    hora = datetime.datetime.time(hora_extraida).hour
    minutos = datetime.datetime.time(hora_extraida).minute
    print(data)
    print(data_atual)
    print(data_atual == data)
    print('-------------')
