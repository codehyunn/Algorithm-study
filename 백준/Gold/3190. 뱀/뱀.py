import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

apple = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K) :
    x,y = map(int, input().split())
    apple[x][y] = 1

L = int(input())
change = deque([tuple(input().split()) for _ in range(L)])

snake = [[False for _ in range(N+1)] for _ in range(N+1)]

x,y,time,d_idx = 1,1,0,0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

snake_tail = deque([(x,y)])
snake[x][y] = True

while True :
    if change and int(change[0][0]) == time :
        change_time, direction = change.popleft()
    
        if direction == 'D' :
            d_idx += 1
            
        elif direction == 'L' :
            d_idx -= 1
            
        d_idx %= 4
    
    x += dx[d_idx]
    y += dy[d_idx]
    time += 1

    if x < 1 or x > N or y < 1 or y > N or snake[x][y]:
        break
     
    snake_tail.append((x,y))
    snake[x][y] = True
    
    if apple[x][y] :
        apple[x][y] = 0
        
    else :
        tail_x, tail_y = snake_tail.popleft()
        snake[tail_x][tail_y] = False
        
print(time)