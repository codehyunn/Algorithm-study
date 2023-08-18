import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, costs, graph) :
    costs[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))

    while queue : 
        cur_cost, cur_node = heapq.heappop(queue)
        
        if cur_cost > costs[cur_node] :
            continue
        
        for next_node, next_cost in graph[cur_node] :
            new_cost = cur_cost + next_cost
            
            if costs[next_node] > new_cost :
                costs[next_node] = new_cost
                heapq.heappush(queue,(new_cost, next_node))
                      
    return costs
            
n = int(input())
m = int(input())

costs = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(m) :
    start, end, cost = tuple(map(int, input().split()))
    graph[start].append((end, cost))
    
start, end = map(int, input().split())

answer = dijkstra(start, costs, graph)

print(answer[end])
