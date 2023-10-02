import sys
from collections import deque

input = sys.stdin.readline

N,L,R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [1,-1,0,0], [0,0,1,-1]

def bfs(x,y,visited) :
    global move, count
    
    queue = deque([(x,y)])

    while queue :
        r,c = queue.popleft()
        move.append((r,c))
        count += A[r][c]
        
        for i in range(4) :
            sr, sc = r+dr[i], c+dc[i]
            if 0 <= sr < N and 0 <= sc < N and not visited[sr][sc] :
                if L <= abs(A[r][c] - A[sr][sc]) <= R :
                    queue.append((sr,sc))
                    visited[sr][sc] = True
                
day = 0
while True :
    queue = deque([(0,0)])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    total_move, total_count = [], []
    
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] :
                move = []
                count = 0
                visited[i][j] = True
                
                bfs(i,j,visited)
                
                if len(move) == 1 :
                    continue
                
                total_move.append(move)
                total_count.append(count)

    if not total_move or not total_count :
        print(day)
        exit()

    for idx, move in enumerate(total_move) :
        _len, _count = len(move), total_count[idx]
        new_pop = _count//_len
        for (r,c) in move :
            A[r][c] = new_pop
    
    day += 1
        