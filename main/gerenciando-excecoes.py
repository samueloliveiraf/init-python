# lista = [1, 10]


# try:
#     # divisao = 10 / 2

#     # numero = lista[3]
#     arq = open('teste1.txt', 'r')
#     texto = arq.read()
#     # x = a
# except ZeroDivisionError:
#     print('Não pode realizar div por 0')
# except IndexError:
#     print('Error ao acessar um indeci da lista')
# except BaseException as ex:
#     print('Error desconhecido Error: {}'.format(ex))
# else:
#     print('Executa quando não ocorre Exception')
# finally:
#     print('Sempre executa')
#     arq.close()

# bandas_metal = ['Iron Maiden', 'Angra', 'Slayer', 'Megadeth', 'Krisiun']
# nova_banda = 'Caetano Veloso'
# if nova_banda not in bandas_metal:
#     raise InputError('{} não é metal!'.format(nova_banda))

# try:
#     divisao = 10 / 0
# except ArithmeticError:
#     erro = 'Houve um erro ao realizar uma operação aritmética'
# except Exception:
#     erro = 'Ocorreu um erro desconhecido'
# else:
#     erro = False
# finally:
#     if erro:
#         print(erro)
#     else:
#         print(divisao)

class InputError(Exception):
    def __init__(self, message):
        self.message = message


nome = 'Adda'
while True:
    try:
        x = input('Digite um nome: ')
        if x == nome:
            break
        else:
            raise InputError('Nome inválido')
    except InputError as ex:
        print(ex)
