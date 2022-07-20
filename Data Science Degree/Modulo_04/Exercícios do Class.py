<<<<<<< HEAD
import numpy as np

arr = np.arange(50)
print(arr)
print('=' * 40)
arr_atualizado = arr[arr % 2]
print('Opção 1:', arr_atualizado)
print('=' * 40)
arr_atualizado_1 = arr[arr > 5]
print('Opção 2:', arr_atualizado_1)
print('=' * 40)
arr_atualizado_2 = arr[arr <= 10]
print('Opção 3:', arr_atualizado_2)
print('=' * 40)
arr_atualizado_3 = arr[(arr != 1) | (arr != 3)]
print('Opção 4:', arr_atualizado_3)
print('=' * 40)
arr_1 = np.random.randint(0, 100, 15)
print(arr_1)
print('Máx:', np.max(arr_1))
print('Máx index:')
print('Maiores que 10:', arr_1[arr_1 > 10])
print('Entre 10 e 30:')
>>>>>>> 3f17da5 (Projeto Aula)
