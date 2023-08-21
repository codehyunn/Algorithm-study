import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
edges = [0 for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append(b)
    edges[b] += 1
    
queue = deque([])

for i in range(1, n+1) : 
    if not edges[i]:
        queue.append(i)
        
while queue : 
    x = queue.popleft()
    print(x, end = ' ')
    for v in graph[x] :
        edges[v] -= 1
        if not edges[v] :
            queue.append(v)