import sys 
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if maps[i][j] == 2 :
            start = (i,j,0)
            answer[i][j] = 0
            visited[i][j] = True
            
        elif maps[i][j] == 0 :
            answer[i][j] = 0


queue = deque([start])
dx,dy = (1,-1,0,0),(0,0,1,-1)

while queue :
    x,y,cnt = queue.popleft()
    for i in range(4) :
        sx,sy = x+dx[i],y+dy[i]
        if 0<=sx<n and 0<=sy<m and not visited[sx][sy] and maps[sx][sy] == 1:
            visited[sx][sy] = True
            answer[sx][sy] = cnt+1
            queue.append((sx,sy,cnt+1))
    
for ans in answer :
    print(*ans)