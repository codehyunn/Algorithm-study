import sys
import heapq

input = sys.stdin.readline

vertex, edge = map(int,input().split())

graph = [[] for _ in range(vertex+1)]
for _ in range(edge) :
    a,b,c = map(int, input().split())     
    graph[a].append((b,c))
    graph[b].append((a,c))

visited = [False for _ in range(vertex+1)]

queue = []
heapq.heappush(queue, (0,1))
answer = 0

while queue : 
    cost, v = heapq.heappop(queue)
    
    if visited[v] :
        continue
    
    visited[v] = True
    answer += cost
    
    for x, x_cost in graph[v] :
        if not visited[x] :
            heapq.heappush(queue, (x_cost, x))


print(answer)