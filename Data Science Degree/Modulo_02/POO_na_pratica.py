class RegistroBancoDados:
    def __init__(self, identificador):
        self.identificador = identificador

    def gravar(self):
        print('Gravando os dados no banco de dados...')
        print(self)

class Publicacao:
    pass


class Revista(Publicacao):
    pass


class Livro(Publicacao):
    pass


revista = Revista(identificador='123', nome='Superinteressante', qtd_paginas=100, periodicidade='Mensal')
print(str(revista))

livro = Livro(identificador='7841235', nome='Antifrágil', qtd_paginas=700, tipo_capa='dura', autor='Nassim Taleb', periodicidade='Mensal')
print(str(livro))

colecao_livro = LivroColecao()
colecao_livro.buscar_todos_itens()

livro.nome = 'Iludidos pelo acaso'
livro.gravar()

nova_revista = Revista('PLC', 'Placar', 130, 'eventual')
colecao_revista.buscar_todos_itens()
