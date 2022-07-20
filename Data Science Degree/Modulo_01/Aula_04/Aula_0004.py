"""
Faça um script python que dada uma lista de número calcule:
1 - a média de todos os valores
2 - a distância do maior para o menor valor
3 - a distância da média para o menor valor
4 - a distância da média para o maior valor

OBS.: len(lista): retorna o tamanho da lista abs(valor): retorna o valor absoluto de um número.
"""
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
media_list = sum(list_numbers) / len(list_numbers)
maior_menor = max(list_numbers) - min(list_numbers)
dist_media_menor = media_list - min(list_numbers)
dist_media_maior = max(list_numbers) - media_list

dist_index_list = list_numbers.index(max(list_numbers)) - list_numbers.index(min(list_numbers))

print(f'Média: {media_list}\n'
      f'Distância maior para o menor: {maior_menor}\n'
      f'Distância da média para o menor: {dist_media_menor}\n'
      f'Distância da média para o maior: {dist_media_maior}\n'
      f'distância do índice do maior para o menor: {dist_index_list}.')

list_input_values = input('Insira a lista de números sepradados por vírgula: ').split(',')
list_values = []

for value in list_input_values:
    value_square = float(value) ** 2
    list_values.append(str(value_square))

print(", ".join(list_values))

