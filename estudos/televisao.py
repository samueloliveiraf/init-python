class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 0

    def verifica(self):
        if self.ligada:
            self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('A tv está desligada')

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('A tv está desligada')


tele = Televisao()

print('Televisao está ligada?: {}'.format(tele.ligada))

# tele.power()

print('Televisao está ligada?: {}'.format(tele.ligada))

tele.aumenta_canal()

tele.verifica()

tele.aumenta_canal()

print('Canal {}'.format(tele.canal))


class Carro:
    def __init__(self):
        self.motor = 'desligado'
        self.movimento = False

    def ligar(self):
        self.motor = 'ligado'

    def acelerar(self):
        if self.motor == 'ligado':
            self.movimento = True

    def carro_em_movimento(self):
        return self.movimento


carro = Carro()
carro.acelerar()
carro_em_movimento = carro.carro_em_movimento()

print(carro_em_movimento)
