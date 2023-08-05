import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

count = n
for num in nums :
    if num == 1 :
        count -= 1
        continue
    for i in range(num-1, 1, -1) :
        if num % i == 0:
            count -= 1
            break
        
print(count)