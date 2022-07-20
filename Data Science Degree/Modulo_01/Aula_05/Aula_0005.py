input_strs = input(" Insira a lista de números separados por vírgula: ").replace(' ', '')

while not input_strs.replace(',', '').replace('.', '').isdecimal():
    input_strs = input("Houve um erro, caracter inválido,\nInsira a lista de números separados por vírgula: ") \
        .replace(' ', '')
else:
    print("Entrada inválida")

list_input_strs = input_strs.split(',')
list_values = []

count = 0
while count < len(list_input_strs):
    list_values.append(float(list_input_strs[count]) ** 2)
    count += 1

print(list_values)

# Faça um script python que acumule diversos valores inseridos pelo usuário. Esses valores devem ser inseridos um a
# um e quando o usuário digitar um character que não possa ser convertido para um número o programa deve parar e
# imprimir o valor acumulado.
numero = 0
list_numero = []
flag = True
while flag:
    numero = input('Digite um número: ')
    if numero.replace('.', '').replace('-', '').isnumeric():
        list_numero.append(float(numero))
    else:
        flag = False

print(sum(list_numero))

import string

digit_list = string.digits
digits = iter(digit_list)
for algarism in digits:
    print(list(digits))
    print(algarism)

print("O tamanho do iterador após o loop: ", len(list(digits)), ' ', len(digit_list))

while (algarism := next(digits, None)) is not None:
    print(algarism)

# from modulo import function
from sys import getsizeof
from copy import deepcopy

list_ = list(range(10000))
list_iter = iter(list_)
list_sum_divs = []

while (value := next(list_iter, None)) is not None:
    if value % 100 == 0:
        print(getsizeof(list(deepcopy(list_iter))))

# Estudar bibliotecas 'sys' e 'os'

for value in list_iter:
    print(getsizeof(list(deepcopy(list_iter))))

#Dicionários
dict_example1 = {'chave': '1'}

print(type(dict_example1) == dict)
dict_example2 = dict(primeiro=1, segundo=2, terceiro=3)

print(dict_example2)

dict_example3 = dict(zip(['primeiro', 'segundo'], [1, 2]))
print(dict_example3)

eval('2+2')

dict_example_3 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
print(dict_example_3)
#ACESSO A UM DADO DE UM DICIONÁRIO PELA CHAVE
print(f"O valor no dicionario com a chave primeiro é {dict_example_3['primeiro']}")
print(dict_example3.get('primeiro', -1))

#INSERIR UM VALOR EM UM DICIONÁRIO JÁ EXISTENTE:
dict_example_3['quarto'] = 4
print(dict_example_3)

dict_example_3.update({'quinto': 5})
print(dict_example_3)

#REMOVER UM ELEMENTO DE UM DICIONARIO
del dict_example_3['quinto']
print(dict_example_3)

dict_example_3.pop('quarto', None)
print(dict_example_3)

#EXCLUINDO O ULTIMO ELEMENTO
dict_example_3.popitem()
print(dict_example_3)

#PODEMOS TAMBÉM MERGEAR (JUNTAR) OS DADOS DE VÁRIOS DICIONÁRIOS EM UM SÓ.
dict_new = {'terceiro': 3, 'quarto': 4, 'quinto': 5}
dict_example_updated = {**dict_example_3, **dict_new}

dict_example_updated.update({'setimo': 7})
print(dict_example_updated)

#Pesquisar 'lambda', 'reduce' e 'map'
from pprint import pprint

list_data = ['ano, mes, dia, valor', '2020, 01, 01, 150.0']

list_header = list_data[0].replace(' ', '').split(',')
list_values = list_data[1].split(',')

dict_data = dict(zip(list_header, list_values))

print(dict_data)

list_data = [['ano, mes, dia, valor', '2020, 01, 01, 150.0'],
             ['ano, mes, dia, valor', '2020, 01, 02, 250.0'],
             ['ano, mes, dia, valor', '2020, 01, 03, 20.0'],
             ['ano, mes, dia, valor', '2020, 01, 04, 300.0']]

list_dict_data = []
for row in list_data:
    list_header = row[0].replace(' ', '').split(',')
    list_values = row[1].split(',')

    list_dict_data.append(dict(zip(list_header, list_values)))

pprint(list_dict_data)

list_alunos = ['Aluno1', ['Aluno1', 10], 'Aluno1', ['Aluno1', 3], ['Aluno1', 9],
               ['Aluno1', 5], ['Aluno2', 7.5], ['Aluno1', 8], 'Aluno5', ['Aluno1', 3],
               ['Aluno2', 3], ['Aluno2', 3], None, None, 'Aluno2', ['Aluno1', 10], ['Aluno3', 10],
               ['Aluno3', 7], 'Aluno3', 5]
dict_alunos = {}

for value in list_alunos:
    if type(value) == list:
        aluno = value[0]
        if not aluno in dict_alunos:
            dict_alunos[aluno] = [value[1]]
        else:
            dict_alunos[aluno].append(value[1])

for aluno, notas in dict_alunos.items():
    print(aluno, sum(notas) / len(notas))

