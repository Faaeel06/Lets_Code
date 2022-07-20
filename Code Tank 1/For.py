pares = []
for contador in range(0, 1000, 2):
    pares.append(contador)
    print(contador)

print(f'A quantidades de pares nesse intervalor é: {len(pares)}')

numero = int(input('Digite um número: '))
for fatorial in range(numero, 1, -1):
    numero *= (fatorial - 1)

print(numero)

numero = int(input('Digite um número: '))
for contador in range(numero, 0, -1):
    if contador % 2 == 0:
        print(contador)
for negativo in range(0, numero, 1):
    if negativo % 2 == 0:
        inverso = negativo * - 1
        print(inverso)



quantidade = int(input('Digite quantos asteriscos: '))
for asterisco in range(1, quantidade + 1):
    print(f'*' * asterisco)

