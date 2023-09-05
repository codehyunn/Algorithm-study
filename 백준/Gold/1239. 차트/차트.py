import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

ans = 0
for per in list(permutations(nums)) :
    points = []
    for i, p in enumerate(per) :
        if i == 0 :
            points.append(p)
            continue
        points.append(p+points[i-1])

    temp = 0
    half_point = N//2
    for i in range(N-1) :
        for j in range(i+1, N) :
            if points[i] + 50 == points[j] :
                temp += 1
    
    ans = max(ans, temp)
    
print(ans)