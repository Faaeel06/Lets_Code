import networkx as nx
import matplotlib.pyplot as plt
import scipy

g1 = nx.Graph()
g1.add_node(1)
g1.add_node(2)
g1.add_node(3)
g1.add_node(4)
g1.add_node(5)
g1.add_node(6)

g1.add_edge(1, 3)

g1.add_edge(2, 3)
g1.add_edge(2, 5)

g1.add_edge(3, 4)

g1.add_edge(4, 5)
g1.add_edge(4, 6)

g1.add_edge(5, 5)
g1.add_edge(2, 6)

path = [caminho for caminho in nx.all_simple_paths(g1, 1, 6)]
print(path)
path_short = nx.shortest_path(g1, 1, 6)
print(path_short)
path_short_all = [path for path in nx.all_shortest_paths(g1, 1, 5)]
print(path_short_all)

g2 = nx.DiGraph()
for i in range(1, 6):
    g2.add_node(i)

    g2.add_edge(1, 3, weight=1)

    g2.add_edge(2, 3, weight=5)
    g2.add_edge(2, 5, weight=7)

    g2.add_edge(3, 4, weight=4)

    g2.add_edge(4, 5, weight=3)
    g2.add_edge(4, 6, weight=3)

    g2.add_edge(5, 5, weight=2)
    g2.add_edge(2, 6, weight=5)

print(g2)

print(g1.adj)
print(g1.nodes)
print(g1.number_of_nodes())
print(g1.edges)
print(g1.number_of_edges())
nx.draw_networkx(g1)
my_pos = nx.spring_layout(g1, seed=42)
nx.draw_networkx(g1, pos=my_pos)
my_pos = {0: [0.15, 1.5],
          1: [-0.15, -1.5],
          2: [2, 0.5],
          3: [1, 1.3],
          4: [0.558, 0.233],
          5: [0.85, 0.90],
          6: [0, 0]}

m1 = nx.adjacency_matrix(g1)
# print(m1)
print(m1.todense())
# print(m1)

plt.plot(g1)

plt.show()
