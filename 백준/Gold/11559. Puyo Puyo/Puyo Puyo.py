import sys
from collections import deque

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

field = [list(input().rstrip()) for _ in range(12)]

def find(x,y,visited,field) :
    dx,dy = [1,-1,0,0],[0,0,1,-1]

    queue = deque([(x,y)])
    puyos = [(x,y)] 
    
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            sx,sy = x+dx[i],y+dy[i]
            if 0<=sx<12 and 0<=sy<6 and not visited[sx][sy] and field[x][y] == field[sx][sy] :
                puyos.append((sx,sy))
                queue.append((sx,sy))
                visited[sx][sy] = True

    return visited, puyos

def bomb(field, puyos) :
    for x,y in puyos :
        field[x][y] = '.'
    return field

def down(field) :
    dot_count = [0 for _ in range(6)]
    for i in range(11, -1, -1) :
        for j in range(6) :
            if field[i][j] == '.' :
                dot_count[j] += 1
            if dot_count[j] and field[i][j] != '.' :
                field[i+dot_count[j]][j] = field[i][j]
                field[i][j] = '.'
    return field

count = 0
while True :
    fin = True
    visited = [[False for _ in range(6)] for _ in range(12)]

    for i in range(12) :
        for j in range(6) :
            if field[i][j] == '.' and not visited[i][j]:
                continue
            
            visited[i][j] = True
            visited, puyos = find(i,j,visited,field)
            if len(puyos) < 4 :
                continue
            
            fin = False
            field = bomb(field,puyos)
    
    if fin :
        print(count)
        exit()
        
    field = down(field)   
    count += 1