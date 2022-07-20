num1 = float(input('Digite o primeiro termo: '))
num2 = float(input('Digite o segundo termo: '))

soma = num1 + num2
multiplicacao = soma * num1

print(f'O valor da soma dos termos é {soma} e a multiplicação do resultado pelo primeiro termo é {multiplicacao}')


salario = float(input('Digite o valor atual do salário: R$ '))
porcentagem = float(input('Digite o valor do percentual de reajuste: '))

percentual = porcentagem / 100
reajuste = (percentual * salario) + salario

print(f'O valor atual do salário é: R${salario:.2f} ;\n'
      f'Com o reajuste de {porcentagem}% o novo salário será: R$ {reajuste:.2f}.')


import datetime

nascimento = ''
idade = input('Digite sua idade: ')
confimacao = str(input('Já fez aniversário?[S/N]')).upper().strip()

if confimacao[0] == 'S':
    nascimento = datetime.date.today().year - int(idade[:2])
elif confimacao[0] == 'N':
    nascimento = datetime.date.today().year - int(idade[:2]) - 1
else:
    print('Comando inválido, tente novamente!')

print(f'Você tem {idade[:2]} anos e nasceu em {nascimento}')

num = float(input('Digite um número: '))

dobro = num * 2
quadrado = num ** 2
cubo = num ** 3

print(f'O número digitado foi: {num};\n'
      f'O dobro do número {num} é: {dobro};\n'
      f'O quadrado do número {num} é: {quadrado};\n'
      f'O cubro do número {num} é: {cubo}.')
