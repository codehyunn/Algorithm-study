import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

T = int(input())
INF = float('inf')
answers = []

for _ in range(T) :
    k = int(input())
    nums = list(map(int, input().split()))
    
    dp = [[INF for _ in range(k)] for _ in range(k)]
    
    for j in range(k) : # 간격
        for i in range(k-j) : # 시작지점
            if j == 0 :
                dp[i][i+j] = 0
                continue
            
            if j == 1 :
                dp[i][i+j] = nums[i] + nums[i+j]
                continue
                
            _sum = sum(nums[i:i+j+1])
            for x in range(j) :
                dp[i][i+j] = min(dp[i][i+j], dp[i][i+x]+dp[i+x+1][i+j]+_sum)
                
    answers.append(dp[0][-1])

for ans in answers :
    print(ans, end='\n')