import sys

input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

left, right = 0, N-1
ans = [nums[left], nums[right]]
min_sum = 2000000000

while left < right :
    _sum = nums[left] + nums[right]
    if abs(_sum) < min_sum : 
        min_sum = abs(_sum)
        ans = [nums[left], nums[right]]
        
    if _sum > 0 :
        right -= 1
    elif _sum < 0 :
        left += 1
    else : 
        break
    
print(*ans)