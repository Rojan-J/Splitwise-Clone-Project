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

            x1, y1 = pos[u]
            x2, y2 = pos[v]
            label_pos = (x2 - 0.1 * (x2 - x1), y2 - 0.1 * (y2 - y1))  # Adjust the 0.1 factor as needed

            # Add the label near the arrowhead
            plt.text(
                label_pos[0], label_pos[1], f"w={capacity}",
                fontsize=12, color='black', ha='center', va='center'
            )
        
        plt.tight_layout()

        plt.title(f"Financial Graph of group {self.graph_name}")
        png_path = "C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_plot.png"
        plt.savefig(png_path)
        plt.show()








