import sys 
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

before = s[0] 
count = 0 if before == 'O' else 1
answer = 0 
pn = 2*n+1

for i in range(1, m) :
    if before == s[i] :
        count = 0 if before == 'O' else 1
        continue
    
    before = s[i]
    count += 1
    if count == pn : 
        answer += 1
        count -= 2
        
print(answer)