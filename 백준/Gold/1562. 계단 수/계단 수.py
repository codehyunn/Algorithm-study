# 계단 수
# 자릿수가 1씩 차이나며 0-9까지의 숫자(10개)가 모두 등장해야함

import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())

if n < 10 :
    print(0)
    exit()

dp = [[defaultdict(int) for _ in range(10)] for _ in range(n)]

for i in range(n) :
    for j in range(10) :
        if i == 0 :
            if j == 0 :
                continue
            dp[i][j][0|(1 << j)] += 1
            
        else :
            if j > 0 :
                for key, value in dp[i-1][j-1].items() :
                    dp[i][j][key | (1 << j)] += value              
            
            if j < 9 :
                for key, value in dp[i-1][j+1].items() :
                    dp[i][j][key | (1 << j)] += value

answer = 0
for dicts in dp[-1] :
    for key, value in dicts.items() :
        if key == 2**10-1 :
            answer += value
            
print(answer%1000000000)