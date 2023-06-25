import sys
input = sys.stdin.readline
N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, N+1) :
    for n in range(10) :
        if 0 <= n-1 <= 9 :
            dp[i][n] += dp[i-1][n-1]
        if 0 <= n+1 <= 9 :
            dp[i][n] += dp[i-1][n+1]
            
print(sum(dp[-1])%1000000000)