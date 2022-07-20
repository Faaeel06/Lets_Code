from pprint import pprint


def convert_lat_long(value: str):
    """Converte a latitude e longitude para float.

    Args:
        value (str): valor da latitude ou longitude de string.

    Returns:
        float: valor em float
    """
    factor = 1 if value[-1] in ['N', 'E'] else -1
    return factor * float(value[:-1])


def read_csv(path_csv_file: str):
    """Método responsável pela leitura de arquivos csv.

    Args:
        path_csv_file (str): caminho do arquivo csv que será lido

    Returns:
        list(str): lista com os as linhas do arquivo texto em forma de strings
    """
    list_resp = []
    with open(path_csv_file, 'r') as file:
        list_resp = [row.replace('\n', '') for row in file.readlines()]

    return list_resp


def convert_row_to_dict(row: list, header: list):
    """Método responsável por converter 

    Args:
        row (list): lista com strings que serão os valores do dicionário
        header (list): lista com strings que serão as chaves do dicionário

    Returns:
        dict: lista com as linhas em forma de dicionários
    """
    return {header[i]: row[i] for i in range(len(header))}


def convert_rows_to_dict(rows: list):
    """Método responsável por converter uma lista de strings que representam linhas de um CSV
    em uma lista onde cada linha é um dicionário.

    Args:
        rows (list): linhas de um arquivo CSV em forma de string.

    Returns:
        list(dict): lista com os dicionários.
    """
    data = []
    if len(rows) > 0:
        header = rows.pop(0).replace('\n', '').split(',')
        for row in rows:
            list_row = row.replace('\n', '').split(',')
            dict_row = convert_row_to_dict(list_row, header)
            data.append(dict_row)

    return data


# QUESTÃO 01
# Implemente uma função de nome group_by onde os argumentos sejam: uma lista de strings que são as linhas
# de um csv e o nome da coluna a ser agrupado os valores.

def group_by(data: list, column_name: str):
    """Este método agrupa os valores da lista rows que estejam em dicionário a partir de uma 
    coluna passada como parâmetro chamado column_name

    Args:
        rows (list): lista com as linhas 
        column_name (str): caminho do arquivo csv que será lido

    Returns:
        dict: dicionário com as chaves sendo os valores de agrupamento e os valores sendo
        uma lista com os dicionários que possuem o valor da chave a qual ele está agrupado.
    """

    # IMPLEMENTE AQUI O CÓDIGO
    dict_group_by = {}
    for dict_values in data:
        for key, values in dict_values.items():
            if key == column_name:
                if not values in dict_group_by:
                    dict_group_by[values] = [dict_values]
                else:
                    dict_group_by[values].append(dict_values)
            else:
                continue

    return dict_group_by


# QUESTÃO 02
# Implemente um método que escreva os dados em um arquivo csv. Os argumentos da função são
# dados é uma lista composta por dicionários que representam as linhas de um CSV e o caminho
# (com o nome do arquivo) que será salvo.

def write_csv(data: list, path_file: str):
    """Método responsável por escrever 

    Args:
        data (list): lista com os dicionários que representam as linhas de um CSV.
        path_file (str): [description]
    """

    # IMPLEMENTE AQUI O CÓDIGO
    header = []
    list_rows = []
    for rows in data:
        list_row = []
        for key, value in rows.items():
            if key not in header:
                header.append(key)
            list_rows.append(value)

        list_row.append('\n')
        list_row = ",".join(list_row)
        list_rows.append(list_row)
    header.append("\n")
    header = ",".join(header)
    list_rows.insert(0, header)

    with open(path_file, "w") as file:
        file.writelines(list_rows)


# QUESTÃO 03
# Implemente um método que seleciona apenas campos específicos do dicionário que representa
# a linha do arquivo CSV e retornam esses dicionários filtrados em uma lista.
def slice(data: list, columns: list):
    """Método que remove os campos dos dicionários que não estão na lista de colunas passadas como
    argumento.

    Args:
        data (list): lista com os dicionários que representam as linhas de um CSV.
        columns (list): nome das colunas que devem ser mantidas nos dicionários que representam
                        as linhas do CSV.

    Returns:
        list: lista com os dicionários somente com os campos definidos na variável columns
    """

    # IMPLEMENTE AQUI O CÓDIGO
    list_dict_filter = []
    for dict_values in data:
        dict_filter = {}
        for key, value in dict_values.items():
            if key in columns:
                dict_filter[key] = value
            else:
                continue
        list_dict_filter.append(dict_filter)

    return list_dict_filter


# QUESTÃO 04
# Implemente um método que calcula a média das AverageTemperatureFahr ou 
# AverageTemperatureUncertaintyFahr a partir dos dados agrupados pelos campos City ou Country.

def get_mean_of_columns(data, column_grouby, column_mean):
    """Método que calcula a média dos valores da coluna column_mean a partir dos dados (data)

    Args:
        data (list[dict]): 
        column_grouby (str): nome da coluna a ser agrupada
        column_mean (str): nome da coluna a ser calculada a média dos valores

    Returns:
        [dict]: dicionário com as chaves sendo os valores da coluna column_groupby,
                e os valores sendo a média dos valores da coluna column_mean.
    """

    # IMPLEMENTE AQUI O CÓDIGO
    rows_column_group_by = group_by(data, column_grouby)

    dict_mean_group_by_column = {}

    for key_groupby, list_dicts in rows_column_group_by.items():
        sum_columnmean = 0
        count_columnmean = 0
        dict_columnmean = {}

        for dict_values in list_dicts:
            for key, value in dict_values.items():
                if key == column_mean:
                    sum_columnmean += float(value)
                    count_columnmean += 1
                else:
                    continue
            mean_columnmean = sum_columnmean / count_columnmean
            dict_columnmean[column_mean] = mean_columnmean
            dict_mean_group_by_column[key_groupby] = dict_columnmean

    return dict_mean_group_by_column


if __name__ == "__main__":
    rows = read_csv('temperature.csv')
    pprint(rows)
    data = convert_rows_to_dict(rows)

    # QUESTÃO 01
    rows_grouped_by_city = group_by(data, 'City')
    # QUESTÃO 02
    write_csv(data, 'temperature_output_02.csv')
    # QUESTÃO 03
    data_locate = slice(data, ['City', 'AverageTemperatureFahr', 'Latitude', 'Longitude'])
    # QUESTÃO 04
    data_mean = get_mean_of_columns(data, 'City', 'AverageTemperatureFahr')


""" Menção honrosa:
Esse código só foi possível com a ajuda do Jeremias Diefenthäler que tirou um tempo para ajudar na solução do
passo a passo extraindo dúvidas valiosas para mim.!"""