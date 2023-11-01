# 11657 타임머신

import sys

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int,input().split()) # n : 노드, m : 간선의 수
distance =  [INF for _ in range(n+1)]
graph = [list(map(int,input().split())) for _ in range(m)]

distance[1] = 0
for i in range(n) :
    for j in range(m) :
        curr_node, next_node, cost = graph[j] 
        if distance[curr_node] != INF and distance[next_node] > distance[curr_node] + cost :
            distance[next_node] = distance[curr_node] + cost

            if i == n-1 :
                print(-1)
                exit()

for d in distance[2:] :
    print(d) if d != INF else print(-1) 