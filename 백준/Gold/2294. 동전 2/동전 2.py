import sys

#sys.stdin = open('answer.txt','r')
input = sys.stdin.readline

INF = float('inf')

n,k = map(int, input().split())
dp = [INF for _ in range(k+1)]

coins = []
for _ in range(n) :
    coin = int(input())
    if coin <= k :
        dp[coin] = 1
    coins.append(coin)

coins = sorted(list(set(coins)))

for i in range(1, k+1) :
    for coin in coins :
        if coin >= i :
            continue
        dp[i] = min(dp[i], 1+dp[i-coin])
        
print(-1 if dp[-1]==INF else dp[-1])