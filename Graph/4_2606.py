#2606 바이러스

cpt = int(input()) ; line = int(input())
graph = [[0 for _ in range(cpt+1)] for _ in range(cpt+1)]
visited = [False for _ in range(cpt+1)]

for i in range(line):
    a,b = map(int, input().split())
    graph[a][b] = 1 ; graph[b][a] = 1

def bfs(a, graph):
    queue = [a]
    visited[a] = True
    while queue!= [] :
        v = queue.pop(0)
        for i in range(1,len(graph[v])):
            if graph[v][i] == 1 and not visited[i] :
                queue.append(i)
                visited[i] = True
    return visited          

v = bfs(1,graph)
print(v.count(True)-1)


