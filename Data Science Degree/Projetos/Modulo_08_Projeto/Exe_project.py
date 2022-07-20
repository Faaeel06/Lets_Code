import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def read():
    # Iniciando o algoritmo com abertura e visualização do arquivo de forma simples
    caminho_do_arquivo = input("Digite o caminho do arquivo: ")
    read = f"{caminho_do_arquivo}"
    print(read)
    data_read = pd.read_csv(read)

    print(data_read.head())

    # Agora econtrando o separador e definindo o mesmo para organização do arquivo

    separador = input("Digite o separador usado no aquivo: ")

    data_read = pd.read_csv(read, sep=separador)

    return data_read.head()


read()
