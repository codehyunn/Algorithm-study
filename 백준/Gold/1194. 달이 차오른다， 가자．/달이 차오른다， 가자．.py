import sys
from collections import deque

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n,m = map(int, input().split())

miro = []

for i in range(n) :
    row = list(input())
    for j, r in enumerate(row) :
        if r == '0' :
            start = (i,j,0,0)
            
    miro.append(row)

queue = deque([start])
dx, dy = [1,-1,0,0], [0,0,1,-1]
visited = [[ [0] * (1 << 6) for _ in range(m)] for _ in range(n)]

lower, upper = ['a','b', 'c', 'd', 'e', 'f'], ['A', 'B', 'C', 'D', 'E', 'F']
start, end, block, road = '0', '1', '#', '.'

while queue :
    x,y,count,key = queue.popleft()

    for i in range(4) : 
        sx, sy = x+dx[i], y+dy[i]
        if 0<=sx and sx<n and 0<=sy and sy<m and not visited[sx][sy][key]:
            miro_value = miro[sx][sy]
            
            if miro_value == block: 
                continue
            
            visited[sx][sy][key] = 1
            
            if miro_value == end :
                print(count+1)
                exit(0)
            
            elif miro_value == road or miro_value == start :
                queue.append((sx,sy,count+1,key))
            
            elif miro_value in lower :
                new_key = key | (1 << (ord(miro_value)-ord('a')))
                queue.append((sx,sy,count+1,new_key))
                
            elif miro_value in upper and (key & (1<<(ord(miro_value)-ord('A')))):
                queue.append((sx,sy,count+1,key))
                    
print(-1)