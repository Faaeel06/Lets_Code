with open("./modulo_3/exercicios/alunos.csv", "r", encoding="UTF-8") as file:
    lista_alunos = file.readlines()

for linhas in lista_alunos:
    linhas.splitlines()
    print(linhas)


class Arvore:
    '''
    classe pra representar uma árvore
    '''

    def __init__(self, root: int, right, left):
        '''
        root (int): o valor no nó;
        right (Arvore): objeto arvore, que representa a sub-arvore à direita
        left (Arvore): objeto arvore, que representa a sub-arvore à esquera
        '''

        # atributos: raiz, com maximo de 2 filhos, e definir quais são os filhos

        self.raiz = root

        self.direita = right

        self.esquerda = left


tree = Arvore(root=15,
              right=Arvore(root=18,
                           right=Arvore(root=20,
                                        right=None,
                                        left=None),
                           left=Arvore(root=17,
                                       right=None,
                                       left=None)),
              left=Arvore(root=6,
                          right=Arvore(root=7,
                                       right=Arvore(root=13,
                                                    right=None,
                                                    left=None),
                                       left=None),
                          left=Arvore(root=3,
                                      right=Arvore(root=4,
                                                   right=None,
                                                   left=None),
                                      left=Arvore(root=2,
                                                  right=None,
                                                  left=None))))

print(tree.direita.esquerda)

