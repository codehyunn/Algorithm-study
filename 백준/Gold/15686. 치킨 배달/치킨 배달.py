import sys
from itertools import combinations

INF = float('inf')

input = sys.stdin.readline

N,M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken, home = [], []
for i in range(N) :
    for j in range(N) :
        if city[i][j] == 2 :
            chicken.append((i,j))
        elif city[i][j] == 1 :
            home.append((i,j))

total_distance = INF
for chlist in list(combinations(chicken, M)) :
    distance = [INF for _ in range(len(home))]
    for (ch_x, ch_y) in chlist :
        for idx, (x,y) in enumerate(home) :
            distance[idx] = min(abs(ch_x-x)+abs(ch_y-y), distance[idx])

    total_distance = min(total_distance, sum(distance))    
    
print(total_distance)