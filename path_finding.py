import networkx as nx

def dfs_bfs_comparison(G, start_node):
    # Depth First Search
    dfs_path = list(nx.dfs_edges(G, source=start_node))
    print("DFS path:", dfs_path)

    # Breadth First Search
    bfs_path = list(nx.bfs_edges(G, source=start_node))
    print("BFS path:", bfs_path)

    # Compare and document the differences in paths
    # (Explanations will be added in README.md)

if __name__ == "__main__":
    G = nx.path_graph(5)  # Create a simple path graph for example
    dfs_bfs_comparison(G, 0)
