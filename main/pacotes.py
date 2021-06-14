import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    print(response.status_code)

    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 400:
        print('CEP informado é inválido')


if __name__ == '__main__':

    retorna_dados_cep(input('Informe o cep: '))
