import sys

input = sys.stdin.readline
R,C = map(int, input().split())           
                
country_map = []
road = []

for r in range(R) : 
    new_map = list(input().strip())
    country_map.append(new_map)
    for c, x in enumerate(new_map) :
        if x == '.' :
            road.append((r, c))

dx,dy = [1,-1,0,0], [0,0,1,-1]
for x,y in road :
    possible = 0
    for i in range(4) :
        sx, sy = x+dx[i], y+dy[i]
        if 0 <= sx < R and 0 <= sy < C and country_map[sx][sy]=='.':
            possible += 1
    if possible < 2 :
        print(1)
        exit()
print(0)