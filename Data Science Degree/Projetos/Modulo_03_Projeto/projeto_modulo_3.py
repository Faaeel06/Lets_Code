import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import scipy

adjascente = '.Organograma empresa.csv'


class Hierarchy:
    def __init__(self, hierarchy):
        self.matrix_hierarchy = nx.adjacency_matrix(Hierarchy).todense()
        self.file_name = adjascente
        self.hierarchy = hierarchy
        hierarchy = nx.DiGraph()

    def intro_function(self):
        self.hierarchy.add_node('CEO')

        self.hierarchy.add_node('1° Gerente')
        self.hierarchy.add_node('2° Gerente')
        self.hierarchy.add_node('3° Gerente')
        self.hierarchy.add_node('4° Gerente')

        self.hierarchy.add_node('1° Analista')
        self.hierarchy.add_node('2° Analista')
        self.hierarchy.add_node('3° Analista')
        self.hierarchy.add_node('4° Analista')
        self.hierarchy.add_node('5° Analista')
        self.hierarchy.add_node('6° Analista')
        self.hierarchy.add_node('7° Analista')
        self.hierarchy.add_node('8° Analista')
        self.hierarchy.add_node('9° Analista')
        self.hierarchy.add_node('10° Analista')
        self.hierarchy.add_node('11° Analista')
        self.hierarchy.add_node('12° Analista')

        self.hierarchy.add_node('1° Estagiário')
        self.hierarchy.add_node('2° Estágiario')

    def create_paths(self):
        self.hierarchy.add_edge('CEO', '1° Gerente')
        self.hierarchy.add_edge('CEO', '2° Gerente')
        self.hierarchy.add_edge('CEO', '3° Gerente')
        self.hierarchy.add_edge('CEO', '4° Gerente')

        self.hierarchy.add_edge('1° Gerente', '1° Analista')
        self.hierarchy.add_edge('1° Gerente', '2° Analista')
        self.hierarchy.add_edge('1° Gerente', '3° Analista')

        self.hierarchy.add_edge('2° Gerente', '4° Analista')
        self.hierarchy.add_edge('2° Gerente', '5° Analista')
        self.hierarchy.add_edge('2° Gerente', '6° Analista')

        self.hierarchy.add_edge('3° Gerente', '7° Analista')
        self.hierarchy.add_edge('3° Gerente', '8° Analista')
        self.hierarchy.add_edge('3° Gerente', '9° Analista')

        self.hierarchy.add_edge('4° Gerente', '10° Analista')
        self.hierarchy.add_edge('4° Gerente', '11° Analista')
        self.hierarchy.add_edge('4° Gerente', '12° Analista')

        self.hierarchy.add_edge('1° Analista', '1° Estagiário')
        self.hierarchy.add_edge('1° Analista', '2° Estagiário')

    def search_paths(self, into_path, end_path):
        self.into_path = into_path
        self.end_path = end_path
        best_path = [caminho for caminho in nx.all_simple_paths(self.hierarchy, self.into_path, self.end_path)]

        return best_path

    def plot_graph(self):
        self.my_pos = nx.spring_layout(Hierarchy, seed=42)
        self.my_pos = {'CEO': ([-0.02391629, 0.02572836]),
                       '1° Gerente': ([0.16817471, 0.17366959]),
                       '2° Gerente': ([-0.1965717, -0.11078105]),
                       '3° Gerente': ([-0.1795172, 0.18091597]),
                       '4° Gerente': ([0.09821963, -0.1562835]),
                       '1° Analista': ([0.25122011, 0.30364427]),
                       '2° Analista': ([0.27413209, 0.25373062]),
                       '3° Analista': ([0.31459987, 0.21631783]),
                       '4° Analista': ([-0.32762752, -0.10399752]),
                       '5° Analista': ([-0.30917148, -0.19734623]),
                       '6° Analista': ([-0.221881, -0.23865048]),
                       '7° Analista': ([-0.31213357, 0.19281515]),
                       '8° Analista': ([-0.18850337, 0.31074164]),
                       '9° Analista': ([-0.2794416, 0.28078891]),
                       '10° Analista': ([0.08102733, -0.28336403]),
                       '11° Analista': ([0.17658635, -0.27327144]),
                       '12° Analista': ([0.22117236, -0.18852557]),
                       '1° Estagiário': ([0.32860288, 0.33428617]),
                       '2° Estágiario': ([-0.24122339, -1.]),
                       '2° Estagiário': ([0.3662518, 0.27958132])}
        nx.draw_networkx(Hierarchy, pos=self.my_pos)
        plt.plot(nx.spring_layout(Hierarchy))

        return plt.show()

    def matrix_ajd_Graph(self, matrix_hierarchy):
        df = pd.DataFrame(matrix_hierarchy, columns=list(self.hierarchy.nodes), index=list(self.hierarchy.nodes))
        df.to_csv('Oganograma Empresa.csv')
        return df



