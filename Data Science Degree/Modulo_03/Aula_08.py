class GrafoMtzAdj:

    def __init__(self, n: int):

        self.ma = [[0] * n for _ in range(n)]

    def __repr__(self):

        return "\n".join(str(x) for x in self.ma)

    def add_edge(self, origin, destiny, direct, weight):

        self.ma[origin][destiny] = weight

        if not direct:
            self.ma[destiny][origin] = weight


if __name__ == '__main__':

    separador = '=' * 15
    g = GrafoMtzAdj(3)
    print(g)
    print(separador)
    g.add_edge(0, 0, direct=True, weight=2)
    g.add_edge(1, 0, direct=True, weight=1)
    g.add_edge(2, 0, direct=True, weight=0)
    g.add_edge(0, 1, direct=True, weight=-7)
    g.add_edge(1, 1, direct=True, weight=0)
    g.add_edge(2, 1, direct=True, weight=1)
    g.add_edge(0, 2, direct=True, weight=1)
    g.add_edge(1, 2, direct=True, weight=1)
    g.add_edge(2, 2, direct=True, weight=1)
    print(g)
    print(separador)
