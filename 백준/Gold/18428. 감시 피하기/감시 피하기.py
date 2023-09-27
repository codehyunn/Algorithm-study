import sys
from itertools import combinations

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

N = int(input())
world = [list(input().split()) for _ in range(N)]

nothing, teacher = [], []
for i in range(N) :
    for j in range(N) :
        if world[i][j] == 'X' :
            nothing.append((i,j))
        elif world[i][j] == 'T' :
            teacher.append((i,j))

for obs in list(combinations(nothing, 3)) :
    for (x,y) in obs :
        world[x][y] = 'O'
    
    avoid = True
    for (tx, ty) in teacher :
        for i in range(tx+1, N) :
            if world[i][ty] == 'S' :
                avoid = False
                break
            
            elif world[i][ty] == 'O' :
                break
               
        for i in range(tx-1, -1, -1) :
            if world[i][ty] == 'S' :
                avoid = False
                break
            
            elif world[i][ty] == 'O' :
                break
        
        for i in range(ty+1, N) :
            if world[tx][i] == 'S' :
                avoid = False
                break
            
            elif world[tx][i] == 'O' :
                break

        for i in range(ty-1, -1, -1) :
            if world[tx][i] == 'S' :
                avoid = False
                break
            
            elif world[tx][i] == 'O' :
                break
        
    if avoid :
        print('YES')
        exit()
          
    for (x,y) in obs :
        world[x][y] = 'X'
        
print('NO')