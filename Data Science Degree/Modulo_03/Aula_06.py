class Arvore:
    """
    classe para repr. uma árvore
    """

    def __init__(self, root=int, right=None, left=None, level=int):
        """
        root(int): o valor do nó
        right(Arvore): objeto arvore, que representa a sub-arvore que está à direita
        left(Arvore): objeto arvore, que representa a sub-arvore que está à esquerdda
        """
        # atributos: raiz, máx. duas ramificações e definir temos ramificados

        self.raiz = root

        self.direita = right

        self.esquerda = left

        self.nivel = level

    def __repr__(self):

        if self.direita is None and self.esquerda is None:

            return f"Folha com valor {self.raiz} no nó."

        elif self.nivel == 0:

            return f"Árvore com o nó raiz de valor {self.raiz}"

        else:

            return f"Árvore com valor {self.raiz} no nó."

    def busca_binaria(self, buscado):

        if buscado == self.raiz:

            return True

        elif self.esquerda == None and self.direita == None:

            return False

        elif buscado < self.raiz:

            self.esquerda.busca_binaria(buscado)

        elif buscado > self.raiz:

            self.direita.busca_binaria(buscado)


tree = Arvore(root=15,
              right=Arvore(root=18,
                           right=Arvore(root=20,
                                        right=None,
                                        left=None,
                                        level=2),
                           left=Arvore(root=17,
                                       right=None,
                                       left=None,
                                       level=2),
                           level=1),
              left=Arvore(root=6,
                          right=Arvore(root=7,
                                       right=Arvore(root=13,
                                                    right=None,
                                                    left=None,
                                                    level=3),
                                       left=None,
                                       level=2),
                          left=Arvore(root=3,
                                      right=Arvore(root=4,
                                                   right=None,
                                                   left=None,
                                                   level=3),
                                      left=Arvore(root=2,
                                                  right=None,
                                                  left=None,
                                                  level=3),
                                      level=2),
                          level=1),
              level=0)

print(tree.direita.esquerda)
