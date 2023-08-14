import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

S = int(input())

_sum = 0
num = 1
count = 0
while _sum <= S :
    if _sum + num <= S :
        _sum += num
        num += 1
        count += 1
        
    else :
        break
    
print(count)