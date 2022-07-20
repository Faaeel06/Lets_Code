class Hora:

    def __init__(self, hour, minute, sec):
        self.h = hour
        self.m = minute
        self.s = sec

    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __str__(self):
        return f'Horário: {self.h:02d}:{self.m:02d}:{self.s:02d}'

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

        return Hora(ho, mi, se)


class Ponto:

    def __init__(self):
        self.lista_horarios = []
        import datetime
        print(datetime.time())

    def banco_Hora_funcionario(self, Hora):  # Armazena todas as entradas de horário do usuário e gera um banco de
        # informações

        lista_horarios = [Hora.entrada_Ponto(), Hora.saida_almoco(), Hora.saida_almoco(), Hora.saida_Ponto()]

        periodo_trabalho = (lista_horarios[0] + lista_horarios[-1])
        periodo_intervalo = (lista_horarios[2] - lista_horarios[1])

        print(f'Tempo de pausa: {periodo_intervalo}\n'
              f'Período Trabalhado: {periodo_trabalho}')

        periodo_trabalho = (lista_horarios[0] + lista_horarios[-1])
        periodo_intervalo = (lista_horarios[1] + lista_horarios[2])

        if periodo_trabalho > '10:00:00':
            return print('você excedeu as horas de trabalho.')

        if periodo_intervalo < '01:00:00':
            return print('Ainda não é hora de voltar.')

        return print(f'Início expediente: {lista_horarios[0]}'
                     f'Início horário almoco: {lista_horarios[1]}'
                     f'Final horário almoço: {lista_horarios[2]}'
                     f'Final expediente: {lista_horarios[3]}'
                     )

    def entrada_Ponto(self=Hora):  # Armazena dados de horário do início dp expediente do usuário

        self.h = int(input('Hora: '))
        self.m = int(input('Minutos: '))
        self.s = int(input('Segundos: '))

        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def saida_almoco(self=Hora):  # Armazena dados de horário do saída da pausa do usuário

        self.h = int(input('Hora: '))
        self.m = int(input('Minutos: '))
        self.s = int(input('Segundos: '))

        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def retorna_almoco(self=Hora):  # Armazena dados de horário do retorno da pausa do usuário

        self.h = int(input('Hora: '))
        self.m = int(input('Minutos: '))
        self.s = int(input('Segundos: '))

        return f'{self.h:02d}:{self.m:02d}:{self.s:02d}'

    def saida_Ponto(self=Hora):  # Armazena dados do horário de expediente do usuário

        self.h = int(input('Hora: '))
        self.m = int(input('Minutos: '))
        self.s = int(input('Segundos: '))

        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def sist_naveg(self):
        from time import sleep
        ''' 
        Sistema de navegação de opções de menu 
        - Deverá conter opção de entrada do usuário 
        - Deverá conter opção de entrada e saída do horário de almoço 
        - Deverá conter opção de saída do usuário 
        '''
        menu_opcao = ('\n1 - Ponto Entrada\n'
                      '2 - Ponto Saída Almoço\n'
                      '3 - Ponto Volta Almoço\n'
                      '4 - Ponto Saída\n'
                      '0 - Fechar Sistema de Ponto\n')
        print(menu_opcao)
        sleep(0.5)
        self.opcao = int(input('\nSelecione a opção desejada: '))
        sleep(0.5)
        while self.opcao != 0:
            if self.opcao == 1:  # Recebe a entrada de horário que o usuário chega na empresa
                self.entrou = P.entrada_Ponto()
                print(self.entrou)
            elif self.opcao == 2:  # Recebe entrada de horário ao sair para o horário de almoço
                self.almoco_in = P.saida_almoco()
                print(self.almoco_in)
            elif self.opcao == 3:  # Recebe a entrada de horário ao voltar do horário volta do almoço
                self.almoco_out = P.retorna_almoco()
                print(self.almoco_out)
            elif self.opcao == 4:  # Recebe a entrada de horário que usuário sair da empresa
                self.saiu = P.saida_Ponto()
                print(self.saiu)
            else:
                print('Opção inválida!')
                P.banco_Hora_funcionario()

            print(menu_opcao)
            sleep(0.5)
            self.opcao = int(input('\nSelecione a opção desejada:  '))

        return


if __name__ == '__main__':
    P = Ponto()
    P.sist_naveg()
    Ponto.banco_Hora_funcionario()
