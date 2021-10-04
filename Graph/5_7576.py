#7576 토마토

from collections import deque
m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [1,-1,0,0],[0,0,1,-1]

def bfs(q):
    while q:
        v = q.popleft()
        for i in range(4) :
            a,b = v[0],v[1]
            x,y = a+dx[i],b+dy[i]
            if n>x>=0 and m>y>=0 and tomato[x][y] == 0 and visited[x][y] == 0:
                q.append([x,y])
                visited[x][y] = visited[a][b] + 1
                tomato[x][y] = 1

    ans = max(map(max,visited))
    return ans

q=deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1 :
            q.append([i,j])

cnt = bfs(q)
for i in range(n):
    if 0 in tomato[i]:
        cnt = -1
    
print(cnt)

