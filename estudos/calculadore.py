calculadora = {
    'soma': lambda a, b: a + b,
    'divisao': lambda a, b: a / b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b
}

soma = calculadora['soma']

print(soma(10, 10))
