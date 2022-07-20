class Quadrado:

    def __init__(self, size, color):
        self.lado = size

        self.cor = color

    def fala_cor(self):
        print(f'Eu sou um quadrado de cor {self.cor}')

    def calcula_area(self):
        return self.lado ** 2


meu_quadrado = Quadrado(4, 'Verde')

print(meu_quadrado.lado)
print(meu_quadrado.cor)
print(meu_quadrado.fala_cor())
print(meu_quadrado.calcula_area())
