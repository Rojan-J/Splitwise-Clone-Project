import networkx as nx
from graph import *
import numpy as np
from collections import deque

class GraphSimplification:
    def __init__(self, graph : Graph):
        self.graph = graph
        self.nodes = list(self.graph.graph.nodes())
        self.n = len(self.nodes)
        self.node_map = {name: idx for idx, name in enumerate(self.nodes)}
        self.residual = np.zeros((self.n, self.n))
        self.level = []
        self.final_simplified_graph = nx.MultiDiGraph()
        self.final_cost = None

    def cycle_simplification(self, scc):
        subgraph = self.graph.graph.subgraph(scc)
        
        # Calculate net balances for each node
        balance = {node: 0 for node in subgraph.nodes}
        for u, v, data in subgraph.edges(data=True):
            balance[u] -= data['capacity']
            balance[v] += data['capacity']
        
        # Create a new simplified subgraph
        simplified_subgraph = nx.MultiDiGraph()
        for node, net_balance in balance.items():
            if net_balance > 0:  # Node is owed money
                for other, other_balance in balance.items():
                    if other_balance < 0 and net_balance > 0:
                        # Transfer the debt to minimize transactions
                        amount = min(net_balance, -other_balance)
                        simplified_subgraph.add_edge(other, node,capacity=amount)
                        balance[node] -= amount
                        balance[other] += amount
        
        return simplified_subgraph
    def cycle_removal(self):
        sccs = list(nx.strongly_connected_components(self.graph.graph))
        for scc in sccs:
            if len(scc) > 1:  # Simplify only non-trivial SCCs (with cycles)
                simplified_scc = self.cycle_simplification(scc)
                self.graph.simplified_graph= nx.compose(self.graph.simplified_graph, simplified_scc)
            else:
                # Copy single-node SCCs (without cycles) as-is
                node = list(scc)[0]
                for u, v, data in self.graph.graph.edges(node, data=True):
                    self.graph.simplified_graph.add_edge(u, v, capacity=data['capacity'])

    def residual_matrix(self):
        for u, v, data in self.graph.simplified_graph.edges(data=True):
            capacity = data.get('capacity', 0)
            self.residual[self.node_map[u]][self.node_map[v]] += capacity
        
        self.final_cost = self.residual.copy()

    def find_level(self, source):
        self.level = np.full(self.n, -1)
        self.level[self.node_map[source]] = 0
        queue = deque([source])

        while queue:
            node = queue.popleft()
            for i in self.nodes:
                if (
                    self.level[self.node_map[i]] == -1
                    and self.residual[self.node_map[node]][self.node_map[i]] > 0
                ):
                    self.level[self.node_map[i]] = self.level[self.node_map[node]] + 1
                    queue.append(i)

    def max_flow_simplifier(self, source, sink):
        flow = 0
        parent = [0] * (self.n)

        def dfs(node):
            if node == sink:
                parent[self.node_map[sink]] = node
                return True
            
            ok = False
            for i in self.nodes:
                if (
                    self.level[self.node_map[i]] == self.level[self.node_map[node]] + 1
                    and self.residual[self.node_map[node]][self.node_map[i]] > 0
                ):
                    if dfs(i):
                        parent[self.node_map[i]] = node
                        ok = True
            return ok
        while True:
            self.find_level(source)
            if self.level[self.node_map[sink]] == -1:
                break
            dfs(source)
            current = sink
            path = []
            while current != source:
                path.append(current)
                current = parent[self.node_map[current]]
            path.append(current)
            path.reverse()

            bottleneck = float("inf")
            for i in range(len(path) - 1):
                bottleneck = min(bottleneck, self.residual[self.node_map[path[i]]][self.node_map[path[i + 1]]])

            for i in range(len(path) - 1):
                self.residual[self.node_map[path[i]]][self.node_map[path[i + 1]]] -= bottleneck

            flow += bottleneck

        return flow, self.residual
    
    def final_simplification(self):
        for i in self.nodes:
            for j in self.nodes:
                if i == j:
                    continue
                max_flow, final_result = self.max_flow_simplifier(i, j)
                if max_flow > 0:
                    self.final_cost = final_result
                    self.final_cost[self.node_map[i]][self.node_map[j]] += max_flow
    

    def to_graph(self):
       self.cycle_removal()
       self.residual_matrix()
       self.final_simplification()
    
       self.final_simplified_graph.add_nodes_from(self.nodes)
       for i in self.nodes:
        for j in self.nodes:
            if self.final_cost[self.node_map[i]][self.node_map[j]] > 0:
                self.final_simplified_graph.add_edge(i, j, capacity = self.final_cost[self.node_map[i]][self.node_map[j]] )

        self.graph.simplified_graph = self.final_simplified_graph




debts_graph = Graph(group_1)
debts_graph.plot_graph()
graph_simplifier = GraphSimplification(debts_graph)
graph_simplifier.to_graph()
debts_graph.graph_type = "simplified"
debts_graph.plot_graph()



    