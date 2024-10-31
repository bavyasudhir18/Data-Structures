# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:57:27 2024

@author: Dell 3380
"""
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[float('inf')] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
        else:
            print("Invalid edge.")

    def floyd_warshall(self):
        # Initialize the distance matrix
        distance = [[float('inf')] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    distance[i][j] = 0
                elif self.adj_matrix[i][j] != float('inf'):
                    distance[i][j] = self.adj_matrix[i][j]

        # Main Floyd-Warshall logic
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]

        return distance

    def display_graph(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(lambda x: f"{x:7}", row)))

        print("\nEdges with Weights:")
        for u in range(self.size):
            for v in range(self.size):
                if self.adj_matrix[u][v] != float('inf'):
                    print(f"{u} -> {v}: {self.adj_matrix[u][v]}")

def main():
    size = int(input("Enter the number of vertices: "))
    g = Graph(size)
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge as: start_vertex end_vertex weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)
    
    print("\nFloyd-Warshall Algorithm results:\n")
    distance_matrix = g.floyd_warshall()
    for row in distance_matrix:
        print(" ".join(map(lambda x: f"{x:7}", row)))
    
    g.display_graph()

if __name__ == "__main__":
    main()
