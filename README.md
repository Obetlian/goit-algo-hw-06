# Graph Algorithms Homework

## Overview
This project implements and analyzes graph algorithms using Python's NetworkX library. The focus is on creating a graph to model a real-world network and applying various algorithms to explore its characteristics and find paths.

---

## Task 1: Graph Creation and Analysis
We modeled a **city's transportation network** as an **undirected weighted graph**. The graph was visualized using Matplotlib, and its basic characteristics like **vertices, edges, and degrees** were analyzed.

✅ **Implemented Features:**
- Graph construction with nodes and weighted edges
- Basic graph analysis (number of nodes, edges, and vertex degrees)
- **Visualization** using NetworkX and Matplotlib

---

## Task 2: Path Finding (DFS & BFS)
We implemented **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** manually and compared their paths in a sample graph.

✅ **Implemented Features:**
- **Manual DFS & BFS implementations** (without NetworkX functions)
- **Comparison of paths** produced by DFS and BFS
- **Graph visualization** to illustrate traversal order

### **🔍 DFS vs. BFS Comparison**
| Feature         | Depth-First Search (DFS) | Breadth-First Search (BFS) |
|---------------|-----------------|-----------------|
| **Approach**  | Goes as deep as possible before backtracking | Explores neighbors level-by-level |
| **Speed**  | Faster for deep graphs | Faster for wider graphs |
| **Use Case** | Best for **pathfinding in mazes**, **solving puzzles** | Best for **shortest path search**, **network traversals** |

✅ **Key Findings:**
- **DFS** tends to find paths that are not necessarily the shortest.
- **BFS** always finds the shortest path in an **unweighted** graph.

---

## Task 3: Dijkstra’s Algorithm for Shortest Path
We implemented **Dijkstra's Algorithm manually** using a **priority queue (heap)** to find the shortest path in a weighted graph.

✅ **Implemented Features:**
- **Manual Dijkstra algorithm** (without NetworkX functions)
- **Priority queue (heap) optimization** for shortest-path computation
- **Visualization** of the graph and its shortest paths

### **🔍 Dijkstra Algorithm Complexity**
| Operation | Complexity |
|-----------|------------|
| **Heap-based Dijkstra** | `O((V + E) log V)` |
| **Adjacency List Storage** | `O(V + E)` |

✅ **Key Findings:**
- **Dijkstra’s Algorithm** efficiently finds the shortest path in **weighted graphs**.
- **BFS cannot be used in weighted graphs** since it does not consider edge weights.
- **Using a priority queue (heap)** makes Dijkstra significantly faster.

---

## 📌 How to Run the Project

```bash
# Run DFS and BFS comparison
python dfs_bfs_comparison.py

# Run Dijkstra Algorithm
python dijkstra_manual.py
