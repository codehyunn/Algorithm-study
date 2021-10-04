#1012 유기농 배추

def bfs(a,b,graph,visited):
    queue = [[a,b]]
    visited[a][b] = True
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    while queue != [] :
        v = queue.pop(0)
        a,b = v[0],v[1]
        for i in range(4):
            x,y = a+dx[i], b+dy[i]
            if 0<=x<m and 0<=y<n and graph[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                queue.append([x,y])

t = int(input())
for i in range(t) :
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    for i in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n) :
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j,graph,visited)
                cnt += 1
    print(cnt)
