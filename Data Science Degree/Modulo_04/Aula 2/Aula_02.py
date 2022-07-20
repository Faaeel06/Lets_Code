import numpy as np
separador = '-=-' * 40

print(separador)
print('3.1')
lista = [1, 2, 3, 4, 5, 6]
meu_array = np.array(lista)
print(meu_array)
meu_array_2 = np.array(lista, dtype=float)
print(meu_array_2)
esp = f'\n'

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
minha_matriz = np.array(matriz)
print(minha_matriz)

print(separador)
print('3.2')
print(esp, list(range(10)))
print(esp, np.arange(10))
print(esp, np.zeros((3, 10)))
print(esp, np.ones((10, 10)))
print(esp, np.full(10, 20))
print(esp, np.empty(4))

print(esp, np.linspace(0, 10, num=5))

print(separador)
print('3.3')
print(esp, np.loadtxt('meu_array.txt', delimiter=','))

print(separador)
print('4.0')
print(esp, np.ones((100, 400)))
print(esp, meu_array.ndim)
print(esp, minha_matriz.ndim)
print('-' * 10)
print(esp, meu_array.size)
print(esp, minha_matriz.size)
print('-' * 10)
print(esp, meu_array.shape)
print(esp, minha_matriz.shape)

print(separador)
print('5.0')
minha_lista = np.array([1, 2, 3, 4, 5, 6])
print(esp, minha_lista[1])
print(esp, minha_lista[4])
print(esp, minha_lista[-2])
print(esp, minha_lista[0:4])
print(esp, minha_lista[1:5])
print(esp, minha_lista[-3:])

print(esp, 'FILTROS')
validacao = [True, True, True, False, False, True]
v_ou_f = [True, False, True, False, True, False]
v_ou_f_array = np.array(v_ou_f)
print(esp, v_ou_f_array)
print(esp, minha_lista[v_ou_f_array])
print(esp, minha_lista % 2 == 0)
print(esp, minha_lista[minha_lista % 2 == 0])
print(esp, minha_lista[minha_lista < 4])

print(separador)
print('6.0')
multpl_array = np.array([1, 2]) * 1.6
print(esp, multpl_array)
print(esp, np.zeros(10) + 1)
print(esp, np.zeros(10) + 6)

print(separador)
print('7.0')
count = 0
sum_ = 0
for i in [1, 2, 3, 4, 5, 6]:
    sum_ += i
    count += 1

print(esp, (sum_/count), esp)

max_ = max([1, 2, 3, 4, 5, 6])
for i in range(len([1, 2, 3, 4, 5, 6])):
    if [1, 2, 3, 4, 5, 6][i] == max_:
        print(i)


max_1 = max([1, 2, 7, 4, 5, 6])
for i in range(len([1, 2, 7, 4, 5, 6])):
    if [1, 2, 7, 4, 5, 6][i] == max_1:
        print(i)

array_1 = np.arange(5)
print(esp, array_1)

print(esp, array_1.sum())
print(esp, array_1.max())
print(esp, array_1.min())
print(esp, array_1.mean())
print(esp, array_1.argmax())

array_2 = np.array([0, 1, 2, 5, 6, 3])
print(esp, array_2.sum())
print(esp, array_2.max())
print(esp, array_2.min())
print(esp, array_2.mean())
print(esp, array_2.argmax())

minha_list = [1, 4, 5, 10, 12]

minha_list_acum = []
sum_1 = 0

for i in minha_list:
    sum_1 += i
    minha_list_acum.append(sum_1)

print(esp, minha_list_acum)

meu_array_03 = np.array(minha_list)
print(esp, meu_array_03)
print(esp, meu_array_03.cumsum())

print(esp, 'COMPARANDO ARRAY COM LISTA')
import random
import time


minha_lista_5 = [random.randint(0, 100) for i in range(10000000)]
meu_array_5 = np.random.randint(0, 100, 10000000)
# print(esp, minha_lista_5)
# print(esp, meu_array_5)

print(len(minha_lista_5), meu_array_5.shape)
inicio_1 = time.time()
soma = 0
for el in minha_lista_5:
    soma += el
fim_1 = time.time()

inicio_2 = time.time()
sum(minha_lista_5)
fim_2 = time.time()

inicio_3 = time.time()
meu_array_5.sum()
fim_3 = time.time()

print(f'Tempo FOR: {(fim_1 - inicio_1)}\n'
      f'Tempo SUM:{(fim_2 - inicio_2)}\n'
      f'Tempo ARRAY: {(fim_3 - inicio_3)}')

print(f'Diferença SUM/FOR: {((fim_1 - inicio_1) / (fim_2 - inicio_2)) :.0f}\n'
      f'Diferença ARRAY/FOR: {((fim_1 - inicio_1) / (fim_3 - inicio_3)) :.0f}\n'
      f'Diferença ARRAY/SUM: {((fim_2 - inicio_2) / (fim_3 - inicio_3)) :.0f}')
