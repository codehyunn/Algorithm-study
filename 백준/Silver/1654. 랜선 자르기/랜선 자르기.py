import sys
input = sys.stdin.readline

k,n = map(int, input().split())
lines = list(int(input()) for _ in range(k))

start, end = 0, max(lines)
answer = 0

while start <= end :
    mid = (start + end) // 2
    if mid == 0 :
        mid = end 
    
    total = 0
    for line in lines :
        if line >= mid :
            total += (line//mid)
    
    if total < n :
        end = mid - 1
    
    else :
        answer = mid
        start = mid + 1
        
print(answer)