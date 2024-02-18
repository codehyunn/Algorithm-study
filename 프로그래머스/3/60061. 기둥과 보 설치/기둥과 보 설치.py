def solution(n, build_frame):
    wall = [[[False,False] for _ in range(n+1)] for _ in range(n+1)]
    
    dx, dy = [0, 0, 1, 1], [0, -1, 0, -1]
    d = [-1, 1]
    
    for x,y,a,b in build_frame :
        # 설치
        if b == 1 : 
            wall[x][y][a] = True
            possible = True 
            
            if a == 0 :
                possible = check_column(x,y,n,wall)
            else :
                possible = check_row(x,y,n,wall)
                
            if not possible :
                wall[x][y][a] = False
            
            continue
                
        # 삭제
        wall[x][y][a] = False
        possible = True
        
        if a == 0 : 
            for i in range(4) :
                sx, sy = x-dx[i], y-dy[i]
                if 0 <= sx < n and 0 <= sy < n+1 and wall[sx][sy][1]:
                    possible = check_row(sx,sy,n,wall)
                    if not possible :
                        break
                        
            if possible :   
                for i in range(2) :
                    sy = y+d[i]
                    if 0 <= sy < n+1 and wall[x][sy][0]:
                        possible = check_column(x,sy,n,wall)
                        if not possible :
                            break
        else : 
            for i in range(4) :
                sx, sy = x+dx[i], y+dy[i]
                if 0 <= sx < n+1 and 0 <= sy < n+1 and wall[sx][sy][0] :
                    possible = check_column(sx,sy,n,wall)
                    if not possible :
                        break
                        
            if possible :      
                for i in range(2) :
                    sx = x+d[i]
                    if 0 <= sx < n and wall[sx][y][1]:
                        possible = check_row(sx,y,n,wall)
                        if not possible :
                            break
        
        if not possible :
            wall[x][y][a] = True
    
    answer = []
    for x in range(n+1) :
        for y in range(n+1) :
            for a in range(2) :
                if wall[x][y][a] :
                    answer.append([x,y,a])
                
    return answer

def check_column(x,y,n,wall) :
    if y == 0 :
        return True
    elif wall[x][y][1] :
        return True
    elif 0 <= y-1 and wall[x][y-1][0] :
        return True
    elif 0 <= x-1 and wall[x-1][y][1] :
        return True
    else :
        return False
    
def check_row(x,y,n,wall) :
    if 0 <= y-1 and wall[x][y-1][0] :
        return True
    elif 0 <= y-1 and x+1 < n+1 and wall[x+1][y-1][0] :
        return True
    elif 0 <= x-1 and x+1 < n and wall[x-1][y][1] and wall[x+1][y][1] :
        return True
    else :
        return False