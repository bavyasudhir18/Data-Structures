# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:13:37 2024

@author: Dell 3380
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i (uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y (uses union by rank)
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimum_cost)

def main():
    V = int(input("Enter number of vertices: "))
    g = Graph(V)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as: start_vertex end_vertex weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)

    print("Kruskal's Minimum Spanning Tree (MST):")
    g.kruskal_mst()

if __name__ == "__main__":
    main()
