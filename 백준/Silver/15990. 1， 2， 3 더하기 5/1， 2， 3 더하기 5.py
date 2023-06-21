import sys

input = sys.stdin.readline
T = int(input())

N_list = []
for i in range(T) :
    N_list.append(int(input()))
N_max = max(N_list)
    
dp = [[0,0,0] for _ in range(N_max+1)]
dp[1], dp[2], dp[3] = [1,0,0], [0,1,0], [1,1,1]

for i in range(4,N_max+1) :
    dp[i] = [(dp[i-1][1]+ dp[i-1][2])%1000000009, (dp[i-2][0]+dp[i-2][2])%1000000009, (dp[i-3][0]+dp[i-3][1])%1000000009]

for n in N_list :
    print(sum(dp[n])%1000000009)
