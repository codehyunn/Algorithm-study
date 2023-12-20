import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase) :
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    
    indegrees = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for _ in range(k) :
        a, b = map(int,input().split())
        indegrees[b] += 1
        graph[a].append(b)
    
    w = int(input())
    
    queue = deque([])
    for i in range(1,n+1) : 
        if indegrees[i] == 0 :
            queue.append(i)
    
    total_times = [times[i] for i in range(n+1)]
    
    while queue :
        x = queue.popleft()
        
        for v in graph[x] :
            indegrees[v] -= 1 
            total_times[v] = max(total_times[v], total_times[x]+times[v])
            
            if indegrees[v] == 0 :
                queue.append(v)        
                
    print(total_times[w])