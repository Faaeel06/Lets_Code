from pprint import pprint


def read_csv(path_csv_file):
    list_resp = []
    with open(path_csv_file, 'r') as file:
        list_resp = [row.replace('\n', '') for row in file.readlines()]

    return list_resp


list_rows_file = read_csv('temperature_1.csv')


def convert_row_to_dict(row: list, header: list):
    return {header[i]: row[i] for i in range(len(header))}


def convert_rows_to_dcit(rows: list):
    data = []
    if len(rows_1) > 0:
        header = rows_1.pop(0).replace('\n', '').split(',')

        for row in rows_1:
            list_row = row.replace('\n', '').split(',')
            dict_row = convert_row_to_dict(list_row, header)
            data.append(dict_row)

    return data


if __name__ == '__main__':
    rows_1 = read_csv('temperature_1.csv')
    data = convert_rows_to_dcit(rows_1)
    pprint(data)
