# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:30:15 2024

@author: Dell 3380
"""

import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
        
    def printMST(self, parent, key):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", key[i])
            total_weight += key[i]
        print(f"Minimum Spanning Tree : {total_weight}")

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v, weight in self.adj_list[u]:
                if not mstSet[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u

        self.printMST(parent, key)

def main():
    V = int(input("Enter number of vertices: "))
    g = Graph(V)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as: start_vertex end_vertex weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)
    
    print("Prim's Minimum Spanning Tree (MST):")
    g.primMST()

if __name__ == "__main__":
    main()
