import matplotlib.pyplot as plt


class Hierarchy:
    """
    Classe para representar a hieraquia dentro de uma empresa, por níveis de cargos
    Apresenta a posição e o superior diramente ligado ao cargo
    """

    def __init__(self, left, middleleft, middle, middleright, right, level):
        """
        left = representa a ponta da extrema-esquerda da árvore
        middleleft = representa todos os nós à esquerda da árvore que não estão no extremo à esquerda
        middle = representa um nó central na árovre também repsenta a raiz(rooot) da árvore
        rightmiddle = representa todos os nós à direita da árovre que não extão no extremo à direita
        right = represnta os nós na extrema direta da árvore
        """

        self.esquerda = left
        self.meio_esquerda = middleleft
        self.meio = middle
        self.meio_direita = middleright
        self.direita = right
        self.nivel = level

    def __repr__(self):
        tree = plt.plot()
        plt.show()

        return tree


hierarchy_tree = Hierarchy(left=Hierarchy(left=Hierarchy(left=None,
                                                         middleleft=None,
                                                         middle='Analista',
                                                         middleright=None,
                                                         right=None,
                                                         level=2),
                                          middleleft=Hierarchy(left=None,
                                                               middleleft=None,
                                                               middle='Analista',
                                                               middleright=None,
                                                               right=None,
                                                               level=2),
                                          middle='Gerente',
                                          middleright=Hierarchy(left=None,
                                                                middleleft=None,
                                                                middle='Analista',
                                                                middleright=None,
                                                                right=None,
                                                                level=2),
                                          right=None,
                                          level=1),
                           middleleft=Hierarchy(left=None,
                                                middleleft=Hierarchy(left=None,
                                                                     middleleft=None,
                                                                     middle='Analista',
                                                                     middleright=None,
                                                                     right=None,
                                                                     level=2),
                                                middle='Gerente',
                                                middleright=Hierarchy(left=None,
                                                                      middleleft=None,
                                                                      middle='Analista',
                                                                      middleright=None,
                                                                      right=None,
                                                                      level=2),
                                                right=Hierarchy(left=None,
                                                                middleleft=None,
                                                                middle='Analista',
                                                                middleright=None,
                                                                right=None,
                                                                level=2),
                                                level=1),
                           middle="CEO",
                           middleright=Hierarchy(left=Hierarchy(left=None,
                                                                middleleft=None,
                                                                middle='Analista',
                                                                middleright=None,
                                                                right=None,
                                                                level=2),
                                                 middleleft=Hierarchy(left=None,
                                                                      middleleft=None,
                                                                      middle='Analista',
                                                                      middleright=None,
                                                                      right=None,
                                                                      level=2),
                                                 middle='Gerente',
                                                 middleright=Hierarchy(left=None,
                                                                       middleleft=None,
                                                                       middle='Analista',
                                                                       middleright=None,
                                                                       right=None,
                                                                       level=2),
                                                 right=None,
                                                 level=1),
                           right=Hierarchy(left=None,
                                           middleleft=Hierarchy(left=None,
                                                                middleleft=None,
                                                                middle='Analista',
                                                                middleright=None,
                                                                right=None,
                                                                level=2),
                                           middle='Gerente',
                                           middleright=Hierarchy(left=None,
                                                                 middleleft=None,
                                                                 middle='Analista',
                                                                 middleright=None,
                                                                 right=None,
                                                                 level=2),
                                           right=Hierarchy(left=None,
                                                           middleleft=Hierarchy(left=None,
                                                                                middleleft=None,
                                                                                middle='Estagiário',
                                                                                middleright=None,
                                                                                right=None,
                                                                                level=3),
                                                           middle='Analista',
                                                           middleright=Hierarchy(left=None,
                                                                                 middleleft=None,
                                                                                 middle='Estagiário',
                                                                                 middleright=None,
                                                                                 right=None,
                                                                                 level=3),
                                                           right=None,
                                                           level=2),
                                           level=1),
                           level=0)

print()
