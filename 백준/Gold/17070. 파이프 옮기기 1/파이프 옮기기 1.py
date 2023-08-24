import sys

#sys.stdin = open('answer.txt','r')
input = sys.stdin.readline

n = int(input())

graph = [[1 for _ in range(n+1)]]
for _ in range(n) : 
    graph.append([1] + list(map(int, input().split())))

# 0:가로, 1:세로, 2:대각선 
dp = [[[0,0,0] for _ in range(n+1)] for _ in range(n+1)]

dp[1][2][0] = 1

for x in range(1, n+1) :
    for y in range(1, n+1) :
        if x==1 and (y==1 or y==2) :
            continue
        
        if graph[x][y] :
            continue
        
        if not graph[x][y-1] :
            dp[x][y][0] += (dp[x][y-1][0] + dp[x][y-1][2])
        
        if not graph[x-1][y] :
            dp[x][y][1] += (dp[x-1][y][1] + dp[x-1][y][2])
            
        if not graph[x][y-1] and not graph[x-1][y] and not graph[x-1][y-1] :
            dp[x][y][2] += sum(dp[x-1][y-1])
                
print(sum(dp[n][n]))