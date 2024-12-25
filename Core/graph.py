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
        self.graph.add_nodes_from(self.group.members.keys())
        for (u, v), attributes in self.group.debts.items():
            self.graph.add_edge(u, v, capacity=attributes["capacity"], flow=attributes["flow"])

    def plot_graph(self):
        if self.graph_type == "Original": graph = self.graph
        else: graph = self.simplified_graph
        pos = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_size= 400)
        nx.draw_networkx_labels(graph, pos, font_size= 10)
        # Draw edges with different connection styles for parallel edges
        for u, v, data in graph.edges(data=True):
            capacity = data["capacity"]
            rad = 0.2 if data['capacity'] > 0 else -0.2

            nx.draw_networkx_edges(
                graph, pos,
                edgelist=[(u, v)],
                connectionstyle=f'arc3,rad={rad}',  # Alternate arcs
                label=f"w={capacity}"
            )
        edge_label_positions = {}
        edge_labels = {}
        for i, (u, v, data) in enumerate(graph.edges(data=True)):
            label = data['capacity']  # Customize your label

            source, target = np.array(pos[u]), np.array(pos[v])
            midpoint = (source + target) / 2  # Straight-line midpoint
            direction = target - source
            perpendicular = np.array([-direction[1], direction[0]])  # Perpendicular vector
            arc_height = np.linalg.norm(direction) * abs(rad)  # Adjust arc height based on curvature

            # Flip the perpendicular adjustment to ensure it's on the outer curve
            arc_midpoint = midpoint - (arc_height * perpendicular / np.linalg.norm(perpendicular)) * np.sign(rad)

            # Save the arc midpoint as the label position
            edge_label_positions[(u, v)] = arc_midpoint
            edge_labels[(u, v)] = label
            plt.text(arc_midpoint[0], arc_midpoint[1], label, fontsize=10, color='black')
        plt.title(f"Financial Graph of group {self.graph_name}")
        plt.show()


group_1 = Groups("Ronil")
group_1.add_members("Niloo", "jhjkhkjh")
group_1.add_members("Rojan", "jdfjhksjjdhf")
group_1.add_members("Mahshid", "sfjhskjdfhksjhdfkjsh")
group_1.add_members("Mohadeseh", "sdjfjfhskjdfhkjshdfkjahdf")

group_1.add_expenses(100, "Mohadeseh", ["Rojan"])
group_1.add_expenses(60, "Niloo", ["Mohadeseh", "Rojan", "Mahshid"])
group_1.add_expenses(90, "Rojan", ["Mohadeseh", "Niloo", "Mahshid"])


debts_graph = Graph(group_1)


    
