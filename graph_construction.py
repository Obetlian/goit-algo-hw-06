import networkx as nx
import matplotlib.pyplot as plt

def create_visualize_graph():
    # Creating a graph example: City transportation network
    G = nx.Graph()
    edges = [
        ("A", "B", {"weight": 1}),
        ("B", "C", {"weight": 2}),
        ("C", "A", {"weight": 3}),
        ("C", "D", {"weight": 4}),
        ("D", "E", {"weight": 2}),
        ("E", "A", {"weight": 1})
    ]
    G.add_edges_from(edges)

    # Visualization
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    # Analyzing characteristics
    print("Number of vertices:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    print("Degrees of vertices:", dict(G.degree()))

if __name__ == "__main__":
    create_visualize_graph()
