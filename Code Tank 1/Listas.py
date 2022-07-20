lista = []
for entrada in range(0, 10):
    numero = input('Digite um número: ')
    lista.append(numero)
print(lista)
print((lista[::-1]))

lista = []
numero = int(input('Digite um número: '))
for contador in range(0, numero):
    lista.append(contador)
print(lista)

lista_nomes = []
lista_idades = []
for cadastro in range(0, 6):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    lista_nomes.append(nome)
    lista_idades.append(idade)
print(lista_nomes)
print(lista_idades)

lista_pares = []
lista_impares = []

for numeros_analise in range(0, 10):
    numero = int(input('Digite um número: '))
    if numero % 2 == 1:
        lista_impares.append(numero)
    else:
        lista_pares.append(numero)
print(f'A lista de números pares é: {lista_pares}')
print(f'A lista de números ímpares é: {lista_impares}')

lista_numeros = []
numero = ''
print('0(Zero) encerra o código.')
while numero != 0:
    numero = int(input('Digite um número: '))
    lista_numeros.append(numero)

lista_numeros.remove(0)
print(f'Você digitou {len(lista_numeros)} números.')
