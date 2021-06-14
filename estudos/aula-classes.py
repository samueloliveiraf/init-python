
class Calculadora:
    def __init__(self, n1, n2):
        self.valor_a = n1
        self.valor_b = n2

    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b


calc = Calculadora(500, 200)

print(calc.soma())
print(calc.sub())
