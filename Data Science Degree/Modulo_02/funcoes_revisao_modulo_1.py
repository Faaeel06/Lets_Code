import random


def validar_par(num):
    return True if num % 2 == 0 else False


print(validar_par(2013257))

print((lambda num: num % 2 == 0)(2032136))

validar_par_2 = lambda num: num % 2 == 0
print(validar_par_2(203213), validar_par_2(2032136))

numeros_aleatorios = random.sample(population=range(0, 101), k=10)
print(numeros_aleatorios)
print(max(numeros_aleatorios))

k = 10
lista = [random.randint(0, 100) for _ in range(k)]
print(lista)
print(max(lista))


def max_aleatorio():
    import random

    lista = random.sample(population=range(0, 101), k=10)

    print(lista)

    return max(lista)


print(max_aleatorio())


def media_aleatorio(n):
    lista = random.sample(population=range(0, 101), k=n)

    print(lista)

    return sum(lista) / len(lista)


print(media_aleatorio(50))


def media_aleatorio_com_rep(n):
    lista = [random.randint(0, 101) for _ in range(n)]

    print(lista)

    return sum(lista) / len(lista)


print(media_aleatorio_com_rep(250))

lista1 = [1, 4, 3]
lista2 = [3, 5, 1]

if len(lista1) == len(lista2):
    lista_produto = [lista1[i] * lista2[i] for i in range(len(lista1))]
else:
    print("Erro! Comprimentos diferentes!")


def produto_listas(lista1, lista2):
    resposta = ([lista1[i] * lista2[i] for i in range(len(lista1))]
                if len(lista1) == len(lista2)
                else "Erro! Comprimentos diferentes!")
    return resposta


# resolução prof. André
def produto_listas(lista1, lista2):
    return ([lista1[i] * lista2[i] for i in range(len(lista1))]
            if len(lista1) == len(lista2)
            else "Erro! Comprimentos diferentes!")


# resolução prof. Bruno Feitosa
def prod_lista(lista1, lista2):
    return [i * j for i, j in zip(lista1, lista2)]


x = 5
lista = [3, 5, 1]


def multiplica_lista_por_escalar(lista, x):
    return [x * elemento for elemento in lista]


print(multiplica_lista_por_escalar(lista, x))

mple = lambda lista, x: [x * elemento for elemento in lista]

print(mple(lista, x))


def fatorial(n):
    if n > 1:
        return n * fatorial(n - 1)
    elif n == 1 or n == 0:
        return 1


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 10):
    print(f'{n}° termo de  fibonacci: {fibonacci(n)}')


def fibonacci_iterativo(n):
    if n <= 0:
        return "ERRO! Posição inexistente."
    else:
        n = n - 1
        lista_fibo = [1, 1]

    for i in range(2, n + 1):
        lista_fibo.append(lista_fibo[i - 1] + lista_fibo[i - 2])

    return lista_fibo


print(fibonacci_iterativo(10))
