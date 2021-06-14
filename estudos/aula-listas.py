# lista = [10, 3, 15, 2]
# lista_animais = ['cachorro', 'gato', 'rato']

# tupla = (1, 10, 5)

# print(tupla[2])

# print(len(tupla))

# lista.sort()

# print(lista)

# nova_lista = lista_animais * 3

# print(nova_lista)

# print(lista_animais)

# if 'lobo' in lista_animais:
#     print('exite o animal')
# else:
#     print('não exite o animal')
#     lista_animais.append('lobo')

# print(lista_animais)

# lista_animais.pop(1)

# print(lista_animais)


# print(lista_animais)

# print(sum(lista))

# print(max(lista))

# print(max(lista_animais))

# for x in lista_animais:
#     print(x)


# lista = [3, 5, 7, 10, 11]
# resultado = []
# for x in lista:
#     if x % 2 == 1:
#         resultado.append(x)
# print(resultado)

# Tirar duplicidades de listas
# lista = ['cachorro', 'cachorro', 'gato', 'gato']
# print(lista)
# conjunto_animais = set(lista)
# print(conjunto_animais)

valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)

print(resultado)
