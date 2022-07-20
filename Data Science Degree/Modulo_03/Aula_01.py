with open("./arquivos_salvos/arquivo_trabalhado.txt", "w", encoding="UTF-8") as file:
    file.write("Arquivo de Trabalho")

# with open("./arquivos_salvos/arquivo_trabalhado.txt", "r+", encoding="UTF-8") as file:
#     file.write("Nova linha de escrita")

with open("./arquivos_salvos/arquivo_trabalhado.txt", "a", encoding="UTF-8") as file:
    file.write("\n")
    file.write("Nova linha de escrita")
    file.write("\n")
    file.write("Buscando fazer mais")

lista = ["A-", "B-", "C-", "D-"]
with open("./arquivos_salvos/arquivo_trabalhado.txt", "a", encoding="UTF-8") as file:

    for elemento in lista:
        file.write("\n")
        file.write(elemento)
