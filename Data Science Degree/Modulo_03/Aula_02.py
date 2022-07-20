import csv
import pandas as pd

separador_partes = "==" * 100

tabela = ["Aluno Nota1 Nota2 Presença".split(" "),
          ["Rafael", 10, 5.6, 75],
          ["Bella", 8.5, 10, 80],
          ["Manu", 8, 8.0, 50]]

for linha in tabela:
    print(*linha, sep="|\t|")
print(separador_partes)
with open("./arquivos_salvos/notas_alunos.csv", "w", encoding="UTF-8") as file:
    csv.writer(file, delimiter=",", lineterminator="\n") \
        .writerows(tabela)

with open("./arquivos_salvos/notas_alunos.csv", "r", encoding="UTF-8") as file:
    primeira_linha = file.readline()
print(primeira_linha)
print(separador_partes)
with open("./arquivos_salvos/notas_alunos.csv", "r", encoding="UTF-8") as file:
    leitor = csv.reader(file, delimiter=",", lineterminator="\n")

    tabela_lida = [linha for linha in leitor]

print(tabela_lida)
print(separador_partes)

with open("./arquivos_salvos/notas_alunos.csv", "r", encoding="UTF-8") as file:
    conteudo = file.read()

tabela_lida2 = [x.split(',') for x in conteudo.split('\n')[:-1]]
print(tabela_lida2)
print(separador_partes)


# Em qual linha está o Rafael
# O valor da nota 1, somar com valor da nota 2, e dividir por 2

def calc_med_aluno(aluno):
    indice = [linha[0] for linha in tabela_lida]
    print('Alunos cadastrados:\n',
          *indice[1:], sep="\n")

    aluno = str(input(f'\nDigite o nome do aluno: '))

    idx_aluno = indice.index(aluno)
    nota1 = float(tabela_lida[idx_aluno][1])
    nota2 = float(tabela_lida[idx_aluno][2])
    nota_final = (nota1 + nota2) / 2
    print(f'A média do(a) {aluno} é: {nota_final}')


df = pd.read_csv("./arquivos_salvos/notas_alunos.csv")
df_1 = df[df["Aluno"] == "Manu"][["Nota1", "Nota2"]].mean(axis=1).values[0]

df_2 = pd.read_csv("./arquivos_salvos/temperature.csv", sep=',')

if __name__ == '__main__':
    print(df)
    print(df_1)
    print(df_2)
    print(df_2['City'].value_counts())
    print(df_2.groupby["Country", 'year'])[["AverageTemperatureFagr"]].mean()
