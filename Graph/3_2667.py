#2667 단지번호붙이기

import sys

N = int(input())
graph = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(a,b):
    queue = [[a,b]]
    visited[a][b] = True
    cnt = 0
    while queue!=[] :
        v = queue.pop(0)
        cnt += 1
        for i in range(4):
            x, y = v[0]+dx[i], v[1]+dy[i]
            if x >= 0 and x < N and y >= 0 and y < N:
                if graph[x][y] == '1' and not visited[x][y]:
                    queue.append([x,y])
                    visited[x][y] = True
    return cnt

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            c = bfs(i,j)
            cnt.append(c)
            
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)

