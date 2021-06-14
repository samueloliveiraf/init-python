from datetime import date, time, datetime, timedelta


def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime("%c"))
    tupla = ('Segunda', 'Terça', 'Quarta',
             'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    nova_data = data_atual - timedelta(days=365)
    print(nova_data)
    data_viagem = datetime.now() - timedelta(days=1)
    print(datetime.now().weekday())  # retornou 0
    print(data_viagem)
    data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora = time(hour=13, minute=14, second=00)
    print('{} às {}'.format(data, hora))
    data_atual = datetime.now()
    resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(resultado)
    hour = timedelta(hours=15)
    soma = hour + 1
    print(soma)


def trabalhando_data():
    date_atual = date.today()
    print(date_atual.strftime('%d/%m/%Y'))


def trabalando_time():
    horario = time(hour=15, minute=10, second=30)
    print(type(horario))


if __name__ == '__main__':
    # trabalhando_data()
    # trabalando_time()
    trabalhando_datetime()
