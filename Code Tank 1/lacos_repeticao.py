x = 0
while x < 5:
   x += 1
   print(x)

#Algoritmo 1
#x = 1
#while x != 0:
#    print(x)

#Algoritmo 2
#x = 1
#while x != 0:
#    x += 1

#Algortmo 3
#numero = int(input('Ler número: '))
#while numero < 10:
#    print(f'o número é: {numero}')

x = 0
num = int(input('Digite o valor: '))
while x < num:
    x += 1
    print(x)


idade = ''
salario = ''
genero = ''
while 0 != idade != 150 and salario != 0 and genero != ['M', 'F', 'OUTRO']:
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
    genero = str(input('Digite o seu gênero;[M/F/Outro]: ')).upper()

soma = 0
resultado = 0
num = int(input('Digite um número: '))
while num >= resultado:
    soma = soma + resultado
    resultado += 1
print(f'{soma}')
