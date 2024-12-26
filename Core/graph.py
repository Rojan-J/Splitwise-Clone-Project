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
            if u != v:
                self.graph.add_edge(u, v, capacity=attributes["capacity"])

    def plot_graph(self):
        count = 0
        if self.graph_type == "Original": graph = self.graph
        else: graph = self.simplified_graph
        pos = nx.circular_layout(graph)
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
                    label=f"w={capacity}",  
                    arrowsize=25,
                    edge_color= 'skyblue'
                )

        plt.title(f"Financial Graph of group {self.graph_name}")
        plt.show()



group_1 = Groups("Ronil")
group_members = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
for ind in group_members:
    group_1.add_members(ind, "jhjkhkjh")

expenses = [
    {"cost": 120, "paid_by": "Alice", "contributed_by": ["Alice", "Bob", "Charlie"]},
    {"cost": 300, "paid_by": "Bob", "contributed_by": ["Alice", "Bob", "Diana", "Eve"]},
    {"cost": 200, "paid_by": "Charlie", "contributed_by": ["Alice", "Charlie", "Eve", "Frank"]},
    {"cost": 500, "paid_by": "Diana", "contributed_by": ["Bob", "Charlie", "Diana", "Eve", "Frank"]},
    {"cost": 150, "paid_by": "Eve", "contributed_by": ["Alice", "Eve", "Frank"]},
    {"cost": 100, "paid_by": "Frank", "contributed_by": ["Bob", "Charlie", "Diana"]}
]

for expense in expenses:

    for cost, payer, contributers in [list(expense.values())]:
        group_1.add_expenses(cost, payer, contributers)







