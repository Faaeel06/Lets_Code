class Arvore:
    """
    classe para repr. uma árvore
    """

    def __init__(self, answer, right, left, level):
        """
        answer = Pergunta o sintoma
        right(Arvore): objeto arvore, que representa a sub-arvore que está à direita
        left(Arvore): objeto arvore, que representa a sub-arvore que está à esquerdda
        """

        self.pergunta = answer
        self.direita = right
        self.esquerda = left
        self.nivel = level

    def __repr__(self):

        if self.direita == None and self.esquerda == None:

            return f"O diagnóstico é: {self.pergunta}"

        elif self.nivel == 0:

            return f"A primeira pergunta é:  {self.pergunta}."

        else:

            return f"Agora eu pergunto:  {self.pergunta}."

    def diagnostico(self):

        if self.esquerda == None and self.direita == None:

            return f"O dignóstico é: {self.pergunta}"

        else:

            pergunta = f"Você está com {self.pergunta}? [Responda Sim ou Não] "

            resposta = input(pergunta).upper()

            while resposta not in ["SIM", "NÃO"]:
                pergunta = f'Não entendi!\nVocê está com {self.pergunta}?  [Responda Sim ou Não] '
                resposta = input(pergunta).upper()

            if resposta == "SIM":

                return self.direita.diagnostico()

            elif resposta == "NÃO":

                return self.esquerda.diagnostico()


dt = Arvore(answer="mal estar",
            left=Arvore(answer="febre",
                        left=Arvore(answer="dor de cabeça",
                                    left=Arvore(answer="saudável",
                                                left=None,
                                                right=None,
                                                level=3),
                                    right=Arvore(answer="fadiga",
                                                 left=None,
                                                 right=None,
                                                 level=3),
                                    level=2),
                        right=Arvore(answer="mancha",
                                     left=Arvore(answer="virose",
                                                 left=None,
                                                 right=None,
                                                 level=3),
                                     right=Arvore(answer="sarampo",
                                                  left=None,
                                                  right=None,
                                                  level=3),
                                     level=2),
                        level=1),
            right=Arvore(answer="dor de cabeça",
                         left=Arvore(answer="vômito",
                                     left=Arvore(answer="fome",
                                                 left=None,
                                                 right=None,
                                                 level=3),
                                     right=Arvore(answer="infecção intestinal",
                                                  left=None,
                                                  right=None,
                                                  level=3),
                                     level=2),
                         right=Arvore(answer="boca seca",
                                      left=Arvore(answer="falta de café",
                                                  left=None,
                                                  right=None,
                                                  level=3),
                                      right=Arvore(answer="ressaca",
                                                   left=None,
                                                   right=None,
                                                   level=3),
                                      level=2),
                         level=1),
            level=0)
