import networkx as nx
from graph import *


def cycle_removal(graph, scc):
    subgraph = graph.subgraph(scc)
    
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

def find_level()

sccs = list(nx.strongly_connected_components(debts_graph.graph))
for scc in sccs:
    if len(scc) > 1:  # Simplify only non-trivial SCCs (with cycles)
        simplified_scc = cycle_removal(debts_graph.graph, scc)
        debts_graph.simplified_graph= nx.compose(debts_graph.simplified_graph, simplified_scc)
    else:
        # Copy single-node SCCs (without cycles) as-is
        node = list(scc)[0]
        for u, v, data in debts_graph.graph.edges(node, data=True):
            debts_graph.simplified_graph.add_edge(u, v, capacity=data['capacity'])

debts_graph.graph_type = "simplified"
debts_graph.plot_graph()



    