class Horario:
    """
    Classe para apresentar um horário com hora, minuto e segundo
    """

    def __init__(self, hour, minute, sec):
        self.h = hour
        self.m = minute
        self.s = sec

    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __str__(self):
        return f'O horário é: {self.h:02d}:{self.m:02d}:{self.s:02d}'

    def __add__(self, other):

        ho = self.h + other.h
        mi = self.m + other.m
        se = self.s + other.s

        while se >= 60:
            mi = mi + 1
            se = se - 60
        while mi >= 60:
            ho = ho + 1
            mi = mi - 60
        while ho >= 24:
            ho = ho - 24

        return Horario(ho, mi, se)

    def __gt__(self, other):

        if self.h > other.h:
            return True

        elif self.h == other.h and self.m > other.m:
            return True

        elif self.h == other.h and self.m == other.m and self.s > other.s:
            return True

        else:
            return False


if __name__ == '__main__':
    agora_original = Horario(21, 1, 54)
    sai_para_almoco = Horario(12, 37, 54)
    self = Horario(12, 32, 42)
    other = Horario(12, 47, 51)
    volta_do_almoco = sai_para_almoco + Horario(1, 30, 0)
    # print(agora_original.h)
    # print(agora_original.m)
    # print(agora_original.s)
    # print(vars(agora_original))
    print(agora_original)
    print(f'Horário de saída: {sai_para_almoco}')
    print(f'Horário para voltar: {volta_do_almoco}')
    print(self > other)
