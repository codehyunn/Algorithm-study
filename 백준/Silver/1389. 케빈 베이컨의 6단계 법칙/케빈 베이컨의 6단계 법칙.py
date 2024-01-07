import sys

input = sys.stdin.readline

n, m = map(int,input().split()) # 유저, 친구관계 수

INF = int(1e9)
kevin = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1) :
    kevin[i][i] = 0
    
for _ in range(m) :
    a,b = map(int,input().split())
    kevin[a][b] = 1
    kevin[b][a] = 1
    
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            kevin[a][b] = min(kevin[a][b], kevin[a][k]+kevin[k][b])

min_kevin = INF
answer = 0
for i in range(1,n+1) :
    if min_kevin > sum(kevin[i][1:]) :
        min_kevin = sum(kevin[i][1:])
        answer = i

print(answer)