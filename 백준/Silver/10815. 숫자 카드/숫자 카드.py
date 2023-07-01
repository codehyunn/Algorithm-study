import sys

input = sys.stdin.readline

N = int(input())
card_nums = sorted(list(map(int, input().split())))

M = int(input())
is_nums = list(map(int, input().split()))

ans = [0] * M
for i,n in enumerate(is_nums) :
    start, end = 0, N-1
    while start <= end :
        mid = (start+end)//2
        mid_value = card_nums[mid]
        if n < mid_value :
            end = mid-1
        elif mid_value < n :
            start = mid+1
        else :
            ans[i] = 1
            break
        
print(*ans) 