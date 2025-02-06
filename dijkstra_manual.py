import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node

    return shortest_paths, previous_nodes

def create_graph():
    G = nx.Graph()
    edges = [
        ("A", "B", 1), ("B", "C", 2), ("C", "D", 4),
        ("D", "E", 2), ("E", "A", 1), ("C", "A", 3)
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    G = create_graph()
    graph_adj_list = {node: {neighbor: G[node][neighbor]['weight'] for neighbor in G.neighbors(node)} for node in G.nodes()}
    
    shortest_paths, prev_nodes = dijkstra(graph_adj_list, "A")
    
    print("Shortest paths from A:", shortest_paths)
    visualize_graph(G)
