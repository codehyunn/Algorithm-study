import sys  
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n) :
    queue = deque([i])
    visited = [0 for _ in range(n)]
    
    while queue :
        now = queue.popleft()
        for x, pos in enumerate(graph[now]) :
            if pos and not visited[x]:
                queue.append(x)
                visited[x] = 1
                
    print(*visited)