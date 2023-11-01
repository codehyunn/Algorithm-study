# 1865 웜홀

import sys
input = sys.stdin.readline

TC = int(input())
INF = int(1e9)
answers = []
    
for _ in range(TC) :
    N, M, W = map(int, input().split()) # 지점, 도로, 웜홀
    
    edges = []
    for _ in range(M) : # 도로 입력
        a, b, time = map(int,input().split())
        edges.append((a,b,time))
        edges.append((b,a,time))
        
    for _ in range(W) : # 웜홀 입력
        a, b, time = map(int,input().split())
        edges.append((a,b,-time))

    def bellman(start) :
        distance = [INF for _ in range(N+1)]
        distance[start] = 0
        
        for i in range(N) : 
            for j in range(len(edges)) :
                curr_node, next_node, time = edges[j]
                if distance[curr_node] + time < distance[next_node] :
                    distance[next_node] = distance[curr_node] + time
                    
                    if i == N-1 :
                        return 'YES'
                    
        return 'NO'

    answers.append(bellman(1))
        
for ans in answers :
    print(ans)
    