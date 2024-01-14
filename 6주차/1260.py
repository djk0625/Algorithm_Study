from collections import deque
import sys

def DFS(graph, c, visited):
    visited[c] = True
    print(c, end = ' ')
    for i in graph[c]:
        if not visited[i]:
            DFS(graph, i, visited)
            
def BFS(graph, c, visited):
    visited = [False] * (a+1)
    queue = deque([c])
    visited[c] = True
    while queue:
        t = queue.popleft()
        print(t, end = ' ')
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


a, b, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(a+1)]

visited = [False] * (a+1)

for i in range(b):
    n, m = map(int, sys.stdin.readline().split())
    graph[n].append(m)
    graph[m].append(n)
    graph[n].sort()
    graph[m].sort()

DFS(graph, c, visited)
print()
BFS(graph, c, visited)
print()