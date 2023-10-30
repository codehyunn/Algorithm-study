import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

INF = float('inf')

dp = [[INF for _ in range(N)] for _ in range(N)]

for k in range(N) :
    for i in range(N-k) :
        j = i+k
        if i == j :
            dp[i][j] = 0
            continue
        
        for x in range(i, j) :
            row,mid,col = matrix[i][0], matrix[x][1], matrix[j][1]
            dp[i][j] = min(dp[i][j], dp[i][x]+dp[x+1][j]+row*mid*col)

print(dp[0][-1])   