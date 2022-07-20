import numpy as np
lista = [1, 3, 3, 45, 56, 765, 56, 5]
buscador = 45


def busca_binaria(lista, buscador):
    lista = lista.copy()

    while len(lista) == 0:
        idx_metade = len(lista)//2

        elemento_meio = lista[idx_metade]

        if buscador == elemento_meio:

            return True

        elif buscador > elemento_meio:

            lista = lista[idx_metade + 1:]

        else:

            lista = lista[:idx_metade]

    return False


busca_binaria(lista=[1, 3, 3, 45, 56, 765, 56, 5], buscador=45)


lista_1 = np.random.randint(0, 50000, 1000).tolist()

lista_ordenada_1 = sorted(lista_1)
print(lista_ordenada_1)
print(busca_binaria(lista_ordenada_1, 420))
