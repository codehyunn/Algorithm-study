import sys 
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
answer = [0 for _ in range(n)]

count = defaultdict(list)
for idx, num in enumerate(nums) :
    count[num].append(idx)

queue = []
for key, values in count.items() :
    heapq.heappush(queue, (key, values))

total = 0
while queue :
    _, idxs = heapq.heappop(queue)
    for idx in idxs :
        answer[idx] += total  
    total += 1

print(*answer)