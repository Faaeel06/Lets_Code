numero = ''
while numero != 0:
    print('O 0(zero) encerra o programa.')
    numero = int(input('Digite um número: '))

idade = []
salario = []
genero = []
idade_usuario = ''
salario_usuario = ''
genero_usuario = ''
while 0 != idade_usuario != 150 and salario_usuario != 0 and genero_usuario != ['M', 'F', 'OUTRO']:
    idade_usuario = int(input('Digite sua idade: '))
    idade.append(idade_usuario)
    salario_usuario = float(input('Digite seu salário: '))
    salario.append(salario_usuario)
    genero_usuario = str(input('Digite o seu gênero;[M/F/Outro]: ')).upper()
    genero.append(genero_usuario.title())

print(idade)
print('=' * 20)
print(salario)
print('=' * 20)
print(genero)

numero = ''
lista_numero = []
while numero != 0:
    numero = int(input('Digite um número: '))
    lista_numero.append(numero)
print(sum(lista_numero))

divisor = 0
contador = 0

numero = int(input('Informe um número: '))

while divisor < numero:
    divisor += 1
    if numero % divisor == 0:
        contador += 1
        print(f'Divisor: {divisor}')
print(f'Total de dvisores: {contador}')