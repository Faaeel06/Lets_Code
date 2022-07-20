from random import randint, shuffle


def quicksort(lista):

    print(lista)

    if len(lista) <= 1:
        return lista

    lista_esquerda = []
    lista_direita = []
    lista_meio = []

    pivo = lista[randint(0, len(lista) - 1)]

    for elemento in lista:

        if elemento == pivo:

            lista_meio.append(elemento)

        elif elemento < pivo:

            lista_esquerda.append(elemento)

        else:

            lista_direita.append(elemento)

    le_ord = quicksort(lista_esquerda)
    ld_ord = quicksort(lista_direita)

    return le_ord + lista_meio + ld_ord


lista = []
tam_lista = int(input('Quantos números quer gerar? '))
for i in range(0, tam_lista):
    lista.append(i)

shuffle(lista)
print(lista)
print(quicksort(lista=lista))
