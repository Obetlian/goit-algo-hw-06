import networkx as nx

def dijkstra_shortest_path(G, source, target):
    path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
    print("Shortest path from", source, "to", target, ":", path)

if __name__ == "__main__":
    G = nx.path_graph(5)  # Simple path graph for example
    nx.set_edge_attributes(G, {e: {"weight": 1} for e in G.edges()})  # Set all weights to 1 for simplicity
    dijkstra_shortest_path(G, 0, 4)
