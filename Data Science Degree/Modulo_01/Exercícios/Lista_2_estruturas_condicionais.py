usuario = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade - 18 >= 0:
    retorno = 'Você já pode tirar carteira de motorista'
else:
    retorno = 'Você ainda não pode dirigir'

print(f'{retorno}.')

numero_entrada = int(input('Digite um número: '))

if numero_entrada > 0:
    validacao = 'Número positivo'
elif numero_entrada < 0:
    validacao = 'Número negativo'
else:
    validacao = 'Você digitou ZERO\nOu digitou algum caractere inválido'

print(f'{validacao}.')

numero_entrada = int(input('Digite o número: '))

if numero_entrada % 2 == 0:
    validacao = 'Número PAR'
else:
    validacao = 'Número Ímpar'

print(f'{validacao}.')
