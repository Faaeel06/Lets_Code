class Cliente:
    def __init__(self, nome, idade, email, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    def visualizar_infos(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'E-mail: {self.email}')
        print(f'CPF: {self.cpf}')


class Sistema:

    def __init__(self):
        self.cadastro = {}

    def cadastro_cliente(self):
        nome = input('Digite o nome do cliente: ')
        idade = input('Digite a idade do cliente: ')
        email = input('Digite o e-mail do cliente: ')
        cpf = input('Digite o CPF do cliente: ')

        novo_cliente = Cliente(nome, idade, email, cpf)

        self.cadastro[cpf] = novo_cliente

    def alterar_cadastro(self):

        print(f"Chaves disponíveis:\n"
              f'{self.cadastro.keys()}', sep='\n')
        cpf_input = ""

        cpf_input = input('\nQual é o CPF do cliente cujos dados você quer alterar? ')
        quero_alterar = input(" O que deseja alterar? ")
        if quero_alterar == 'nome':
            self.cadastro[cpf_input].nome = input("Qual o novo nome?")
        elif quero_alterar == 'idade':
            self.cadastro[cpf_input].idade = input('Qual a nova idade? ')
        elif quero_alterar == 'email':
            self.cadastro[cpf_input].email = input('Qual o novo e-mail? ')
        elif quero_alterar == 'cpf':
            cpf_novo = input('Qual o novo CPF? ')
            self.cadastro[cpf_input].cpf = cpf_novo
            valor = s.cadastro.pop(cpf_input)
            self.cadastro[cpf_novo] = valor

        print(self.cadastro[cpf_input].visualizar_infos())
        pass

    def visualizar_cadastro(self, cpf):
        pass

    def sist_naveg(self):
        from time import sleep

        print('1 - Cadastrar Cliente\n'
              '2 - Exibir informações do Cliente\n'
              '3 - Alterar dados do Cliente\n'
              '0 - Sair')
        sleep(0.5)
        opcao = int(input('\nO que você deseja fazer? '))
        sleep(0.5)
        while opcao != 0:
            if opcao == 1:
                s.cadastro_cliente()
            elif opcao == 2:
                s.visualizar_cadastro()
            elif opcao == 3:
                s.alterar_cadastro()
            else:
                print('Não entendi!')

                opcao = int(input('\nO que você deseja fazer? '))

        pass


if __name__ == '__main__':
    from time import sleep
    s = Sistema()
    print('=' * 50)
    print('Bem-vindo ao sistema de Cadastro'.center(50))
    print('=' * 50)
    sleep(0.5)
    s.sist_naveg()
    sleep(0.5)
