import sys 

input = sys.stdin.readline
m,n = map(int,input().split())

nums = [1 for _ in range(n+1)]

for i in range(2, n+1) :
    if nums[i] == 0 :
        continue
    
    if i >= m : 
        print(i)
        
    for x in range(2, n//i+1) :
        nums[x*i] = 0