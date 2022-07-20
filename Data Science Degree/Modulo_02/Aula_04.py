class Pessoa:
    """
    Classe de pessoas
    """

    def __init__(self, name, hair_color, height):
        self.nome = name
        self.cor_cabelo = hair_color
        if type(height) != float:
            raise ValueError("Tipo de dado errado para altura!")
        else:
            self.altura = height


gente = Pessoa(name='Bob', hair_color='Dark', height=1.70)
dados_gente = vars(gente)


class Pessoa:
    """
    Classe de pessoas
    """

    def __init__(self, name, hair_color, height):
        self.nome = name
        self.cor_cabelo = hair_color
        if type(height) != float:
            raise ValueError("Tipo de dado errado para altura!")
        else:
            self.altura = height


gente = Pessoa(name='Bob', hair_color='Dark', height=1.70)


class Pessoa:
    """
    Classe de pessoas
    """

    def __init__(self, name, hair_color, height):
        """
        Método construtor inicializa os
        atributos, "nome", "cor_cabelo" e altura
        """
        self.nome = name
        self.cor_cabelo = hair_color

        if type(height) != float:
            raise ValueError("Tipo de dado errado para altura!")
        else:
            self.altura = height

        self.num_passaporte = None
        self.marca_carro = None
        self.num_filhos = 0


Alice = Pessoa('Alice', 'Preto', 1.70)
print(Alice)


class Pessoa:
    """
    Classe de pessoas
    """

    def __init__(self, name, hair_color, height):
        """
        Método construtor inicializa os
        atributos, "nome", "cor_cabelo" e altura
        """
        self.nome = name
        self.cor_cabelo = hair_color

        if type(height) != float:
            raise ValueError("Tipo de dado errado para altura!")
        else:
            self.altura = height

        self.num_passaporte = None
        self.marca_carro = None
        self.num_filhos = 0

    def fala(self, texto):

        self.texto = texto

        print(f"{self.nome}, que tem cabelo cor {self.cor_cabelo} diz:\n{texto}")


Alice = Pessoa('Alice', 'Preto', 1.70)
Alice.fala(texto='Bem-vindo!')


class Pessoa:
    '''
    classe de pessoas
    '''

    def __init__(self, name, hair_color, height):
        '''
        método construtor, inicializa os
        atributos "nome", "cor_cabelo" e "altura"
        "'''

        self.nome = name
        self.cor_cabelo = hair_color

        if type(height) != float:

            raise ValueError("Tipo de dado errado pra altura!")

        else:

            self.altura = height

        self.num_passaporte = None
        self.marca_carro = None
        self.num_filhos = 0

        # bool
        self.emprego = False
        self.salario = 0

    def fala(self, texto):

        print(f"{self.nome}, que tem cabelo cor {self.cor_cabelo} diz:\n{texto}")

    def pinta_cabelo(self, cor):

        self.cor_cabelo = cor

    def status_emprego(self, empregado, salary=0):
        '''
        muda status de emprego, e adiciona respectivo salario
        argumentos:
            - emprego: booleano;
            - salary: int ou float.
        '''

        self.emprego = empregado

        self.salario = salary if empregado else 0

    def aumento(self, perc):
        '''
        aumenta o salario em "perc" pontos percentuais
        OBS: o perc deve estar "dividido por 100",
        ou seja, se houver um aumento de 10%, temos perc = 0.1
        '''

        if self.emprego:

            self.salario = self.salario * (1 + perc)

        else:

            print(f"{self.nome} não tem emprego, portanto, não pode ter aumento!")

if __name__ == '__main__':
    name = input('Digite seu nome: ')
    emprego = None
    salario = 0

    print(f'Emprego: {emprego}\nSalário: {salario}')

    empregado = True
    emprego = input('Digite o cargo: ')
    salary = input('Digite o salário: R$ ')

    salario = salary if empregado else 0

    print(f'Emprego: {emprego}\nSalário: R$ {float(salario):.2f}')
