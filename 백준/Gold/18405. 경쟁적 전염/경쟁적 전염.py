import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
S,X,Y = map(int, input().split())

queue = deque([])
for i in range(N) :
    for j in range(N) :
        if not world[i][j] :
            continue
        n = world[i][j]
        queue.append((n,i,j))


dx, dy = [1,-1,0,0], [0,0,1,-1]

for _ in range(S) :
    if world[X-1][Y-1] or not queue:
        print(world[X-1][Y-1])
        exit()
    
    queue = deque(sorted(queue, key=lambda x:x[0]))
    
    lenq = len(queue)
    for _ in range(lenq) :
        n,x,y = queue.popleft()
        for i in range(4) :
            sx, sy = x+dx[i], y+dy[i]
            if 0<=sx<N and 0<=sy<N and not world[sx][sy] :
                world[sx][sy] = n
                queue.append((n,sx,sy))
                
print(world[X-1][Y-1])