from collections import deque

def solution(maps):
    n, m = len(maps),len(maps[-1])
    
    queue = deque([[0,0]])
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<m :
                if maps[nx][ny] == 1 :
                    queue.append([nx,ny])
                    maps[nx][ny] = maps[x][y] + 1
    
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]