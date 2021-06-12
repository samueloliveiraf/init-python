
class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b


calc = Calculadora()

print(calc.soma(1, 10))
print(calc.sub(5, 3))
