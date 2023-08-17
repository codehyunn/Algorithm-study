import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

gap = n+1
_sum = 0
right = 0

for left in range(n) :
    while right < n :
        _sum += numbers[right]
        
        if _sum >= s :
            gap = min(gap, right-left+1)
            _sum -= (numbers[left] + numbers[right])
            break
        
        right += 1
        
print(gap if gap < n+1 else 0)