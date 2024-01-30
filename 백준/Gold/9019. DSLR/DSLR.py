import sys 
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    a,b = map(int,input().split())
    
    queue = deque([(a,'')])
    
    visited = [False]*10000
    visited[a] = True
    
    while queue :
        n, comm = queue.popleft()
        if n == b :
            print(comm)
            break
        
        d = (2*n) % 10000
        if not visited[d] :
            queue.append((d, comm+'D'))
            visited[d] = True
        
        s = n-1 if n > 0 else 9999
        if not visited[s] :
            queue.append((s, comm+'S'))
            visited[s] = True
            
        l = (n%1000)*10 + n//1000
        if not visited[l] :
            queue.append((l, comm+'L'))
            visited[l] = True
            
        r = (n//10) + (n%10)*1000
        if not visited[r] : 
            queue.append((r, comm+'R'))    
            visited[r] = True