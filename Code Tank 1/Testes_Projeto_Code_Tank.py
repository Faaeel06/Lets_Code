# Logística
#Solução do Professor // Para Estudos
def otimiza_transporte(k, caixas, capacidade=100):
    caixas.sort(reverse=True)
    nao_usado = caixas
    lista_organizada = []
    #Vou iterar para todos os k caminhoes
    for caminhao in range(k):
        soma = 0
        tamanho = len(nao_usado)
        i = 0
        usado = []
        # Checa o peso total do caminhao com a nova caixa estoura o limite
        while soma < capacidade and i < tamanho:
            if soma + nao_usado[i] <= capacidade:
                vlr = nao_usado.pop(i)
                #adiciona caixa ao caminhão
                usado.append(vlr)
                soma += vlr
                tamanho = len(nao_usado)
                i = 0
            else:
                i += 1
        lista_organizada.append(usado)
    #Faz verificação final e imprime a resposta pedido
    if len(nao_usado) > 0:
        print(f'Não tem caminhões suficientes, sobrou {nao_usado}')
    else:
        print(f'Os caminhões serão suficientes, a organização será:\n{lista_organizada}')


k = 2
caixas = [90, 19, 90]
otimiza_transporte(k=k, caixas=caixas)
