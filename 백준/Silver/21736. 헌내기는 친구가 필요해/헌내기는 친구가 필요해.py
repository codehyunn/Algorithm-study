import sys 
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for a in range(n) :
    for b in range(m) :
        if campus[a][b] == 'I' :
            visited[a][b] = True
            start = (a,b)
            break

queue = deque([start])
dx, dy = [1,-1,0,0],[0,0,1,-1]
answer = 0

while queue : 
    x,y = queue.popleft()
    for i in range(4) :
        sx,sy = x+dx[i], y+dy[i]
        if 0<=sx<n and 0<=sy<m and not visited[sx][sy] :
            visited[sx][sy] = True
            if campus[sx][sy] == 'X' :
                continue
            
            queue.append((sx,sy))
            if campus[sx][sy] == 'P' :
                answer += 1

print(answer if answer > 0 else 'TT')