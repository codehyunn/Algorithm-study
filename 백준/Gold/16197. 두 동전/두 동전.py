import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

board = []
coins = []

for i in range(n) :
    row = list(input().strip())
    
    if len(coins) < 4 :
        for ridx, r in enumerate(row) :
            if r == 'o' :
                coins.extend([i, ridx])
                
    board.append(row)
    
queue = deque([tuple(coins+[0])])
dx, dy = [1,-1,0,0], [0,0,1,-1]

visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

while queue :
    x1,y1,x2,y2,cnt = queue.popleft()
    
    if cnt >= 10 :
        print(-1)
        exit()

    for i in range(4) :
        sx1, sy1, sx2, sy2 = x1+dx[i], y1+dy[i], x2+dx[i], y2+dy[i]
        
        if 0<=sx1<n and 0<=sy1<m and 0<=sx2<n and 0<=sy2<m :
            if not visited[sx1][sy1][sx2][sy2] :
                visited[sx1][sy1][sx2][sy2] = True
                
                if board[sx1][sy1] == '#' and board[sx2][sy2] == '#' :
                    continue
                
                if board[sx1][sy1] == '#' :
                    sx1, sy1 = x1, y1
                
                if board[sx2][sy2] == '#' :
                    sx2, sy2 = x2, y2
                    
                queue.append((sx1,sy1,sx2,sy2,cnt+1))
    
        elif (n<=sx1 or sx1<0 or m<=sy1 or sy1<0) and 0<=sx2<n and 0<=sy2<m:
            print(cnt+1)
            exit()
            
        elif (n<=sx2 or sx2<0 or m<=sy2 or sy2<0) and 0<=sx1<n and 0<=sy1<m:
            print(cnt+1)
            exit()
            
print(-1)