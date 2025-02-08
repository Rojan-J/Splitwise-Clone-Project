import networkx as nx
import matplotlib.pyplot as plt

import sys
import os
import numpy as np
sys.path.append(os.path.abspath("./Project/Splitwise-Clone-Project/Models"))

#sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Models"))

# Import the class


class Graph():
    def __init__(self, group):
        self.graph = nx.MultiDiGraph()
        self.group =group
        self.graph_type = "Original"
        self.graph_name = f"{self.graph_type}{self.group.group_name}"
        self.simplified_graph = nx.MultiDiGraph()
        self.CreateGraph()
        self.Net_balance = dict()


    def CreateGraph(self):
        self.graph.add_nodes_from(self.group.members)
        for (u, v), attributes in self.group.debts.items():
            self.graph.add_edge(u, v, capacity=attributes["capacity"])
        for (u, v), attributes in self.group.simplified_debts.items():
            self.simplified_graph.add_edge(u, v, capacity=attributes["capacity"])

    def plot_graph(self):
        count = 0
        if self.graph_type == "Original": graph = self.graph
        else: graph = self.simplified_graph
        pos = nx.spring_layout(graph)
        plt.figure(figsize=(8, 6))
        in_degree_centrality = nx.in_degree_centrality(graph)
        weighted_in_degree = dict(graph.in_degree(weight='capacity'))
        central_node = max(weighted_in_degree, key=weighted_in_degree.get)
        label_colors = {node: 'black' for node in graph.nodes()}
        label_colors[central_node] = "red"


        for node in graph.nodes():
            out_weight = sum(float(f"{d['capacity']:.2f}" )for _, _, d in graph.out_edges(node, data=True))
            in_weight = sum(float(f"{d['capacity']:.2f}") for _, _, d in graph.in_edges(node, data=True))
            self.Net_balance[node] = in_weight - out_weight


        for node, (x, y) in pos.items():
            plt.text(
                x, y,  # Adjust position slightly above the node
                str(node),
                fontsize=15,
                color=label_colors.get(node, 'black'),  # Default to black if no color is defined
                ha='center',
                fontweight = "bold"
            )

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
        
        #png_path = r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core\graph_plot.png"

        
        plt.savefig(png_path)

#"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core"
        








