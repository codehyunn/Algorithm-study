import sys
from collections import deque

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n,m = map(int, input().split())

world = []
for _ in range(m) :
    world.append(list(input().strip()))


def find(team, visited, start) :
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    
    visited[start[0]][start[1]] = True
    queue = deque([start])

    count = 1
    while queue :
        x,y = queue.popleft()
        
        for i in range(4) :
            sx, sy = x+dx[i], y+dy[i]
            
            if 0<=sx<m and 0<=sy<n and not visited[sx][sy] and world[sx][sy] == team:
                queue.append((sx,sy))
                visited[sx][sy] = True
                count += 1
                
    return count, visited
                
visited = [[False for _ in range(n)] for _ in range(m)]
idx_dict = {'W':0, 'B':1}

answer = [0,0]
for i in range(m) :
    for j in range(n) :
        if not visited[i][j] :
            team = world[i][j]
            cnt, visited = find(team, visited, (i,j))
            answer[idx_dict[team]] += cnt**2
            
print(*answer)