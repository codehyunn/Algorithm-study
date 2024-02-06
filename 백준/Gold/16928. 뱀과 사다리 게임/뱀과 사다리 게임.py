import sys  
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

maps = [i for i in range(101)]
visited = [False for _ in range(101)]

for _ in range(n) :
    x,y = map(int,input().split())
    maps[x] = y

for _ in range(m) :
    u,v =map(int,input().split())
    maps[u] = v
    
queue = deque([(1, 0)])
visited[1] = True

answer = 100
while queue :
    x, cnt = queue.popleft()
    if x == 100 :
        answer = min(cnt, answer)
        
    if x+1 <= 100 and not visited[maps[x+1]]:
        visited[maps[x+1]] = True
        queue.append((maps[x+1], cnt+1))
        
    if x+2 <= 100 and not visited[maps[x+2]]:
        visited[maps[x+2]] = True
        queue.append((maps[x+2], cnt+1))
        
    if x+3 <= 100 and not visited[maps[x+3]]:
        visited[maps[x+3]] = True
        queue.append((maps[x+3], cnt+1))
        
    if x+4 <= 100 and not visited[maps[x+4]]:
        visited[maps[x+4]] = True
        queue.append((maps[x+4], cnt+1))
        
    if x+5 <= 100 and not visited[maps[x+5]]:
        visited[maps[x+5]] = True
        queue.append((maps[x+5], cnt+1))
        
    if x+6 <= 100 and not visited[maps[x+6]]:
        visited[maps[x+6]] = True
        queue.append((maps[x+6], cnt+1))

print(answer)