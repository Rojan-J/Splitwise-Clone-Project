import networkx as nx
import matplotlib.pyplot as plt

import sys
import os
import numpy as np
sys.path.append(os.path.abspath("./Project/Splitwise-Clone-Project/Models"))

# Import the class
from groups import Groups


class Graph():
    def __init__(self, group: Groups):
        self.graph = nx.MultiDiGraph()
        self.group =group
        self.graph_type = "Original"
        self.graph_name = f"{self.graph_type}{self.group.group_name}"
        self.simplified_graph = nx.MultiDiGraph()
        self.CreateGraph()


    def CreateGraph(self):
        self.graph.add_nodes_from(self.group.members)
        for (u, v), attributes in self.group.debts.items():
            if u != v:
                self.graph.add_edge(u, v, capacity=attributes["capacity"])

    def plot_graph(self):
        count = 0
        if self.graph_type == "Original": graph = self.graph
        else: graph = self.simplified_graph
        pos = nx.spring_layout(graph)
        plt.figure(figsize=(8, 6))
        nx.draw_networkx_labels(graph, pos, font_size= 15)
        # Draw edges with different connection styles for parallel edges
        
        for u, v, data in graph.edges(data=True):
            if u != v: 
                count += 1
                capacity = data["capacity"]
                rad = 0.2 if data['capacity'] > 0 else -0.2

                nx.draw_networkx_edges(
                    graph, pos,
                    edgelist=[(u, v)],
                    connectionstyle=f'arc3,rad={rad}',  # Alternate arcs
                    label=f"{capacity}",  
                    arrowsize=25,
                    edge_color= 'skyblue'
                )

        plt.tight_layout()
        png_path = "C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_plot.png"
        plt.savefig(png_path)
        plt.show()








