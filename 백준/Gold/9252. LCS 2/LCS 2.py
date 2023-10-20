import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()


dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(a)+1) :
    for j in range(1, len(b)+1) :
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        

lcs_length = max(dp[-1])
print(lcs_length)

if not lcs_length :
    exit()

lcs = ''
i, j = len(a), dp[-1].index(lcs_length)
n = dp[i][j]

while n > 0 and i > 0 and j > 0 :
    if dp[i-1][j] == n :
        i -= 1
    elif dp[i][j-1] == n :
        j -= 1
    else :
        lcs += a[i-1]
        i, j = i-1, j-1
        
    n = dp[i][j]

print(lcs[::-1])