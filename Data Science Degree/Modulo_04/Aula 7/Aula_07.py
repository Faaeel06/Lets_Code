import pandas as pd
from time import sleep

entrada = []
separadores = ['|', '*', '/', '%', '!', '+', '$', '@', '#']


def open_file():
    print('Digite nome do arquivo[sem extensão]:')
    print('Digite o nome e aperte enter')

    for i in range(0, 3):
        entrada.append(input(f'Digite o {i + 1}° arquivo: '))
        entrada[i] += '.csv'
        file = pd.read_csv(entrada[i])
    return


def read_file():
    for file in range(0, len(entrada)):
        arquivo_leitura = pd.read_csv(entrada[file])
        print(arquivo_leitura)


def tratament_file():
    read_file()



if __name__ == '__main__':
    open_file()
    sleep(0.5)
    read_file()
