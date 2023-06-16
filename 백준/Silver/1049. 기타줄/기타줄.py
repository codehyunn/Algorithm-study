N, M = map(int,input().split())

min_package = float('inf')
min_one = float('inf')

for i in range(M) :
    package, one = map(int, input().split())
    if package < min_package :
        min_package = package
    if one < min_one :
        min_one = one
    
dp = [0] * (N+1)

if N < 6 :
    for i in range(1,N+1) :
        dp[i] = i*min_one
else :
    for i in range(1,6) :
        dp[i] = i*min_one

    for i in range(6,N+1) :
        dp[i] = min(min_package+dp[i-6], dp[i-1]+min_one)
        

print(min(dp[-1], min_package*(N//6+1)))
    
