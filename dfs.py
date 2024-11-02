# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:05:20 2024

@author: Dell 3380
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.visited = [False] * vertices

    def add_edge(self, v, w):
        self.adj_list[v].append(w)

    def dfs_util(self, v):
        self.visited[v] = True
        print(v, end=" ")

        for w in self.adj_list[v]:
            if not self.visited[w]:
                self.dfs_util(w)

    def dfs(self, start_vertex):
        for v in range(self.V):
            self.visited[v] = False

        self.dfs_util(start_vertex)

def main():
    V = int(input("Enter number of vertices: "))
    g = Graph(V)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as: start_vertex end_vertex weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v)
    
    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print(f"DFS starting from vertex {start_vertex}: ")
    g.dfs(start_vertex)

if __name__ == "__main__":
    main()
