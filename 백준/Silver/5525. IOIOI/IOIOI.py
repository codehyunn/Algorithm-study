import sys 
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

answer = 0
sn = 'IO'*n + 'I'
lensn = 2*n+1

for i in range(m-lensn+1) :
    if s[i:i+lensn] == sn :
        answer += 1
        
print(answer)