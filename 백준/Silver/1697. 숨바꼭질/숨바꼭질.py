import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

if n > k :
    print(n-k)
    
elif k == n :
    print(0)
    exit()

else :
    visited = [False] * (2*k) 
    visited[n] = True
    
    ans = float('inf')
    queue = deque([(0, n)])
    
    while queue :
        time, pos = queue.popleft()
        
        if pos > k : 
            ans = min(ans, time+pos-k)
            continue
        elif pos == k :
            ans = min(ans, time)
            print(ans)
            break
            
        if pos*2 < 2*k and not visited[pos*2] :
            visited[pos*2] = True
            queue.append((time+1, pos*2))
        if pos+1 < 2*k and not visited[pos+1] :
            visited[pos+1] = True
            queue.append((time+1, pos+1))
        if 0 <= pos-1 and not visited[pos-1] :
            visited[pos-1] = True
            queue.append((time+1, pos-1))