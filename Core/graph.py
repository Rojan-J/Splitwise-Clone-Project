import networkx as nx
import matplotlib.pyplot as plt

import sys
import os

sys.path.append(os.path.abspath("./Project/Splitwise-Clone-Project/Models"))

# Import the class
from groups import Groups


class Graph():
    def __init__(self, group: Groups):
        self.graph = nx.DiGraph()
        self.group =group

    def CreateGraph(self):
        self.graph.add_nodes_from(self.group.members)
        self.graph.add_weighted_edges_from(self.group.expences)

    def plot_graph(self):
        pos = nx.spring_layout(self.graph)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title(f"Financial Graph of group {self.group.name}")
        plt.show()

    
