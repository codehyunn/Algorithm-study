import sys  
input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n+1)]

check = 0
for i in range(1, n+1) :
    if i == (check+1)**2 :
        dp[i] = 1
        check += 1
        continue
    
    for j in range(1, check+1) :
        dp[i] = min(dp[i], dp[i-j**2]+dp[j**2])       

print(dp[-1])