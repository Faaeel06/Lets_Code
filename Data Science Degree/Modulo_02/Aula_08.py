from pprint import pprint


class Retangulo:

    def __init__(self, la, lb):
        self.lado_a = la
        self.lado_b = lb

    def calc_area(self):
        area = self.lado_a * self.lado_b

        return area

    def __str__(self):
        return f'Sou um retângulo de lados {self.lado_a} e {self.lado_b}.'

    def __repr__(self):
        return (("+ " * self.lado_a + '\n') * self.lado_b)[:-1]


class Quadrado(Retangulo):

    def __init__(self, lado):
        super().__init__(la=lado, lb=lado)

    def __str__(self):
        return f'Sou um quadrado de lado {self.lado_a}.'

    def __repr__(self):
        return (("* " * self.lado_a + '\n') * self.lado_b)[:-1]


if __name__ == '__main__':
    r1 = Retangulo(5, 3)
    q1 = Quadrado(5)
    print(r1)
    print(r1.calc_area())
    pprint(r1)
    print(q1)
    print(q1.calc_area())
    pprint(q1)
