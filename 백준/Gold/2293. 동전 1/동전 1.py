n,k = map(int,input().split())
p = [int(input())for _ in range(n)]
dp = [0 for _ in range(k+1)] 


for j in p:
    for i in range(j, k+1):
        if i == j:
            dp[i] = dp[i] + 1
        else:
            dp[i] = dp[i] + dp[i-j]
        
ans = dp[k]
print(ans)