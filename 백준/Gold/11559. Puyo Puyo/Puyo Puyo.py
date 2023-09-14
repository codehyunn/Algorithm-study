import sys

input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]
visited = [[False for _ in range(6)] for _ in range(12)] 

def dfs(x,y,color) :
    global puyos     
    puyos.append((x,y))
    
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    for i in range(4) :
        sx,sy = x+dx[i], y+dy[i]
        if 0<=sx<12 and 0<=sy<6 and not visited[sx][sy] and board[sx][sy] == color:
            visited[sx][sy] = True
            dfs(sx,sy,color)
            
def delete(puyos) :
    for (x,y) in puyos :
        board[x][y] = '.'
        
def down() :
    for j in range(6) :
        row_count = 0
        stop_count = False
        for i in range(11,0,-1) :
            if board[i][j] == '.' :
                row_count += 1
                if board[i-1][j] != '.' :
                    board[i-1+row_count][j] = board[i-1][j]
                    board[i-1][j] = '.'
                    row_count -= 1
        
count = 0
while True :
    puyo_found = False
    visited = [[False for _ in range(6)] for _ in range(12)] 

    for i in range(12) :
        for j in range(6) :
            if not visited[i][j] and board[i][j] != '.':
                visited[i][j] = True
                puyos = []
                
                dfs(i,j,board[i][j])
                
                if len(puyos) >= 4 :
                    delete(puyos)
                    puyo_found = True
    
    if not puyo_found :
        print(count)
        exit()
        
    down()
    count += 1