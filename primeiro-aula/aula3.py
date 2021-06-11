
# a = int(input('Primeiro valor A: '))

# b = int(input('Segundo valor B: '))

# c = int(input('Segundo valor C: '))

# if a > b and a > c:
#     print('O maior número é A = {}'.format(a))
# elif(b > a > c):
#     print('O maior número é B = {}'.format(b))
# else:
#     print('O maior numero é C = {}'.format(c))

# a = int(input('Informe um número: '))

# if a % 2 == 0:
#     print('O numero é par {}'.format(a))
# else:
#     print('O número é ímpar: {}'.format(a))    

# a = int(input('Informe um numero: '))

# b = int(input('Informe um numero: '))

# resto_a = a % 2

# resto_b = b % 2

# # not inverte a condicao

# if resto_a == 0 or not resto_b > 0:
#     print('Tem número par')
# else:
#     print('Não tem número par apenas impar')


n1 = float(input('Informe nota 1: '))

while n1 > 10 or n1 < 0:
    n1 = float(input('Você digitou a nota erra: Informe N1: '))
    

n2 = float(input('Informe nota 2: '))
while n2 > 10 or n2 < 0:
    n2 = float(input('Você digitou a nota erra: Informe N2: '))
   

n3 = float(input('Informe nota 3: '))
while n3 > 10 or n3 < 0:
    n3 = float(input('Você digitou a nota erra: Informe N3: '))
    

n4 = float(input('Informe nota 4: '))
while n4 > 10 or n4 < 0:
    n4 = float(input('Você digitou a nota erra: Informe N4: '))
    

media = (n1 + n2 + n3 + n4)/4

print('Média: {}'.format(media))

if(media >= 7):
    print('aprovado')
elif(media >= 5):
    print('prova final')
else:
    print('reprovado')



