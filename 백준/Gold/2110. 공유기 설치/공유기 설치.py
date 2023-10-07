import sys
input = sys.stdin.readline

n,c = map(int,input().split())
homes = sorted(list(int(input()) for _ in range(n)))

# 집 사이 간격으로 이분 탐색 진행
answer = 0
start, end = 0, homes[-1]

while start <= end :
    mid = (start+end)//2
    
    count = 1
    before, current = 0, 1
    
    while current < n :
        if count > c :
            break
        if homes[before] + mid <= homes[current] :
            before = current
            count += 1
        current += 1
        
    if count < c :
        end = mid - 1
        
    elif count >= c :
        answer = max(answer, mid)
        start = mid + 1

print(answer)