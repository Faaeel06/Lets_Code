# arquivo = open('caminho_do_arquivo', 'modo', 'encoding')


# file_csv = open('temperature_1.csv', mode='r')
# print(file_csv)
# Ver o conteúdo do arquivo
# print(type(file_csv.read()))
# Ver o conteúdo do arquivo já separado em linhas
# display(file_csv.readline())
#
# for row in file_csv.readlines():
#     print(row.replace('\n', ''))
#
# file_csv.close()

# with open('temperature_1.csv', mode='r') as file:
#     rows = file.readlines()
#     for row in rows:
#         print(row)
#
# row_1 = rows[0]
# print(row_1.replace('\n', '').split(','))
#
# with open('arquivo_texto.txt', 'w') as file_writer:
#     file_writer.write("Let's Code\n")
#
# with open('arquivo_texto.txt', 'r') as file_reader:
#     print(file_reader.read())
#
# with open('arquivo_texto.txt', 'a') as file_writer:
#     file_writer.write("Let's Code Degree\t Data Science\n")
#
# with open('arquivo_texto.txt', 'r') as file_reader:
#     print(file_reader.read())
#
# with open('temperature_1.csv', 'r') as file:
#     rows = file.readlines()
#
# header = rows.pop(0)
# rows_Kherson = [row for row in rows if 'Kherson' in row]
# rows_Kherson.insert(0, header)
#
# with open('temperature_Kherson.csv', mode='w') as file:
#     file.writelines(rows_Kherson)
# with open('temperature_Kherson.csv', mode='w') as file:
#     str_lines = ''.join(rows_Kherson)
#     file.write(str_lines)
#
# with open('temperature_1.csv', 'r') as file:
#     rows = file.readlines()
#
# header = rows.pop(0)
# #rows_Auckland = [row for row in rows if 'Auckland' in row]
# rows_Auckland = []
# for row in rows:
#     if 'Auckland' in row:
#         rows_Auckland.append(row)
#
# rows_Auckland.insert(0, header)
#
# with open('temperature_Aukland.csv', mode='w') as file:
#     str_lines = ''.join(rows_Auckland)
#     file.write(str_lines)
#
lista = ["""474544,"01","01","1867",68.5094,33.8522,"Auckland","NEW","New Zealand","36.17S","175.03E" """,
         """474545,"02","01","1867",66.992,33.7244,"Auckland","NEW","New Zealand","36.17S","175.03E" """,
         """3778335,"01","01","1753",22.7066,42.2816,"Kherson","UKR","Ukraine","47.42N","31.97E" """,
         """3778336,"02","01","1753",23.1476,37.1318,"Kherson","UKR","Ukraine","47.42N","31.97E" """]

values = ['Kherson', 'Auckland']
dictionarie = {}
dictionarie[values[0]] = [row for row in lista if 'Kherson' in row]
dictionarie[values[1]] = [row for row in lista if 'Auckland' in row]

for key in dictionarie:
    rows_to_add = dictionarie[key]
    with open(f'temperature_{key.lower()}.csv', 'a+') as file:
        file.writelines([row + '\n' for row in rows_to_add])

# #OUTRO MODO
# dict_cities = {}
# dict_cities['Kherson'] = [row for row in lista if 'Kherson' in row]
# dict_cities['Auckland'] = [row for row in lista if 'Auckland' in row]
#
# for key, rows_by_city in dict_cities.items():
#     with open(f'temperature_{key.lower()}.csv', 'a') as file:
#         str_to_write = '\n'.join(rows_by_city)
#         file.write(str_to_write)
#
# #OUTRO MODO 2
# dict_cities = {'Kherson': [row for row in lista if 'Kherson' in row],
#                'Auckland': [row for row in lista if 'Auckland' in row]}
#
# for key, rows_by_city in dict_cities.items():
#     with open(f'temperature_{key.lower()}.csv', 'a') as file:
#         str_to_write = '\n'.join(rows_by_city)
#         file.write(str_to_write)
#
# data = []
# with open('temperature_1.csv', 'r') as file:
#     rows = file.readlines()
#     header = rows.pop(0).replace('\n', '').split(',')
#
#     for row in rows:
#         list_row = row.replace('\n', '').split(',')
#         dict_row = {header[i]: list_row[i] for i in range(len(header))}
#         data.append(dict_row)
#
# pprint(data[:2])
#
# #OUTRO MODO
# data = []
# rows_1 = []
# with open('temperature_1.csv', 'r') as file:
#     rows_1 = file.readlines()
#
# if len(rows_1) > 0:
#     header = rows_1.pop(0).replace('\n', '').split(',')
#
#     for row in rows_1:
#         list_row = row.replace('\n', '').split(',')
#         dict_row = {header[i]: list_row[i] for i in range(len(header))}
#         data.append(dict_row)
#
# pprint(data[:2])
#
# def read_csv(path_csv_file):
#     list_resp = []
#     with open(path_csv_file, 'r') as file:
#         list_resp = [row.replace('\n', '') for row in file.readlines()]
#
#     return list_resp
#
#
# list_rows_file = read_csv('temperature_1.csv')
#
# pprint(list_rows_file)
#
#
# def convert_row_to_dict(row: list, header: list):
#     return {header[i]: row[i] for i in range(len(header))}
#
#
# def convert_rows_to_dict(rows: list):
#     data = []
#     if len(rows_1) > 0:
#         header = rows_1.pop(0).replace('\n', '').split(',')
#
#         for row in rows_1:
#             list_row = row.replace('\n', '').split(',')
#             dict_row = convert_row_to_dict(list_row, header)
#             data.append(dict_row)
#
#     return data
#
#
# rows_1 = read_csv('temperature_1.csv')
# data = convert_rows_to_dict(rows_1)
