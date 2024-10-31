# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:48:03 2024

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
            print("Invalid.")

    def dijkstra(self, start_vertex):
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None

            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

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

    start_vertex = int(input("Enter the starting vertex for Dijkstra's algorithm: "))
    print(f"\nDijkstra's Algorithm starting from vertex {start_vertex}:\n")

    distances = g.dijkstra(start_vertex)
    for i, d in enumerate(distances):
        print(f"Shortest distance from {start_vertex} to {i}: {d}")

    g.display_graph()

if __name__ == "__main__":
    main()
