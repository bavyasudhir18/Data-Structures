# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:28:43 2024

@author: Dell 3380
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
        else:
            print("Invalid edge.")

    def topological_sort(self):
        visited = [False] * self.size
        stack = []

        def explore(v):
            visited[v] = True
            for u in range(self.size):
                if self.adj_matrix[v][u] != 0 and not visited[u]:
                    explore(u)
            stack.append(v)

        for i in range(self.size):
            if not visited[i]:
                explore(i)

        return stack[::-1]  # Return vertices in topological order

    def shortest_path_dag(self, destination_vertex):
        # Initialize distances with infinity for all vertices except the destination
        distances = [float('inf')] * self.size
        distances[destination_vertex] = 0

        # Get topological order of vertices
        topological_order = self.topological_sort()

        # Process each vertex in reverse topological order
        for u in reversed(topological_order):
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and distances[v] != float('inf'):
                    distances[u] = min(distances[u], self.adj_matrix[u][v] + distances[v])

        return distances

    def display_graph(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))
        
        print("\nEdges with Weights:")
        for u in range(self.size):
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0:
                    print(f"{u} -> {v}: {self.adj_matrix[u][v]}")

def main():
    size = int(input("Enter the number of vertices: "))
    g = Graph(size)

    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge as: start_vertex end_vertex weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)

    destination_vertex = int(input("Enter the destination vertex for the shortest path algorithm: "))
    print(f"\nShortest Path to destination vertex {destination_vertex}:\n")

    distances = g.shortest_path_dag(destination_vertex)
    for i, d in enumerate(distances):
        print(f"Shortest distance to {destination_vertex} from {i}: {d if d != float('inf') else 'Unreachable'}")

    g.display_graph()

if __name__ == "__main__":
    main()
