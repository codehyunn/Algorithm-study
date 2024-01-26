import sys 
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

idxs = defaultdict(list)
for i in range(n) :
    idxs[nums[i]].append(i)

for i, num in enumerate(sorted(set(nums))) :
    for idx in idxs[num] :
        nums[idx] = i

print(* nums)