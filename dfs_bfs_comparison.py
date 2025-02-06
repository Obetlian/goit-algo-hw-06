import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    
    return path

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)
            queue.extend(graph[node] - visited)
    
    return path

def compare_dfs_bfs():
    # Creating a sample graph
    G = nx.Graph()
    edges = [
        ("A", "B"), ("B", "C"), ("C", "D"),
        ("D", "E"), ("E", "A"), ("C", "A")
    ]
    G.add_edges_from(edges)

    # Convert the graph into an adjacency list representation
    graph_adj_list = {node: set(G.neighbors(node)) for node in G.nodes()}

    # Running the manual DFS and BFS
    dfs_path = dfs(graph_adj_list, "A")
    bfs_path = bfs(graph_adj_list, "A")

    print("DFS path:", dfs_path)
    print("BFS path:", bfs_path)

    # Visualization
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2500, font_size=12)
    plt.show()

if __name__ == "__main__":
    compare_dfs_bfs()
