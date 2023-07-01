import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for i in range(T) :
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for i in range(1, M+1) :
        a,b = map(int, input().split())
        graph[a].append((i,b))
        graph[b].append((i,a))
        
    visited = [False] * (N+1)
    flight = [0] * (M+1)
    
    start = graph[1][0]
    start_flight, start_city = start
    
    queue = deque([start])
    visited[start_city] = True
    flight[start_flight] += 1
    
    while queue :
        v = queue.popleft()
        v_flight, v_city = v
        for x_flight, x_city in graph[v_city] :
            if not visited[x_city] :
                queue.append((x_flight, x_city))
                flight[x_flight] += 1
                visited[x_city] = True
    
    ans = len(flight) - flight.count(0)
    
    print(ans)