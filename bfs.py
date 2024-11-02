# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:50:51 2024

@author: Dell 3380
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.value

    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(current.value)
            current = current.next
        return ' -> '.join(map(str, items))

# BFS algorithm
def bfs(adj, s):
    q = Queue()
    visited = [False] * len(adj)
    visited[s] = True
    q.enqueue(s)
    while not q.is_empty():
        curr = q.dequeue()
        print(curr, end=" ")
        for x in adj[curr]:
            if not visited[x[0]]:
                visited[x[0]] = True
                q.enqueue(x[0])

def add_edge(adj, u, v, weight):
    adj[u].append((v, weight))

def main():
    V = int(input("Enter number of vertices: "))
    adj = [[] for _ in range(V)]
    E = int(input("Enter number of edges: "))
    print("Enter each edge as: start_vertex end_vertex weight")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        add_edge(adj, u, v, weight)
    start_vertex = int(input("Enter the starting vertex for BFS: "))
    print(f"BFS starting from vertex {start_vertex}: ")
    bfs(adj, start_vertex)

if __name__ == "__main__":
    main()
