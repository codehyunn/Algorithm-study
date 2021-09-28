#9465 스티커

import sys

t = int(input())
for i in range(t):
    n = int(input())
    u = [0] + list(map(int,input().split()))
    d = [0] + list(map(int,input().split()))
    
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    #dp[0][i] : u, dp[1][i] : d
    
    if n>=1:
        dp[0][1] = u[1]
        dp[1][1] = d[1]
        
    for i in range(2, n+1):
        dp[0][i] = u[i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = d[i] + max(dp[0][i-1], dp[0][i-2])

    score = max(dp[0][n], dp[1][n])
    print(score)

 
