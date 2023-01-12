from collections import deque
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True 
    cnt = 1
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for a,b in wires :
        graph[a].append(b)
        graph[b].append(a)
    
    for start,b in wires :
        visited = [False] * (n+1)
        visited[b] = True
        result = bfs(graph, visited, start)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
    
    return  answer