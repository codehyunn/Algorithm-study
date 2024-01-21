import sys
from collections import deque

input = sys.stdin.readline
m,n,h = map(int,input().split())

tomato = []
ripen_tomato = []
all_ripen = True
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

for x in range(h) :
    temp = []
    for y in range(n) :
        row = list(map(int,input().split()))
        for z in range(m) :
            if row[z] == 1 :
                ripen_tomato.append((0,x,y,z))
                visited[x][y][z] = True
            elif row[z] == 0 :
                all_ripen = False
        temp.append(row)
    tomato.append(temp)

if all_ripen : 
    print(0)
    exit()
    
queue = deque(ripen_tomato)
dx,dy,dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]
answer = 0

while queue : 
    days,x,y,z = queue.popleft()
    answer = max(answer,days)
    
    for i in range(6) :
        sx,sy,sz = x+dx[i], y+dy[i], z+dz[i]
        if 0 <= sx < h and 0 <= sy < n and 0 <= sz < m and not visited[sx][sy][sz] :
            if tomato[sx][sy][sz] == -1 :
                continue
            
            visited[sx][sy][sz] = True
            tomato[sx][sy][sz] = 1
            queue.append((days+1,sx,sy,sz))
                
for a in range(h) :
    for b in range(n) :
        for c in range(m) :
            if tomato[a][b][c] == 0 : 
                print(-1)
                exit()

print(answer)