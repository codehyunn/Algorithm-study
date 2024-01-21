import sys
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

n, m = map(int, input().split())

graph  = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v) :
    visited[v] = True
    for x in graph[v] :
        if not visited[x] :
            dfs(x)

count = 0   
for i in range(1, n+1) :
    if not visited[i] :
        dfs(i)
        count += 1

print(count)