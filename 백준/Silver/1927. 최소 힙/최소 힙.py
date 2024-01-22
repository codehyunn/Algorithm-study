import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n) :
    nums.append(int(input()))
    
queue = []

for num in nums :
    if num == 0 :
        if not queue :
            print(0)
        else :
            print(heapq.heappop(queue))
    else :
        heapq.heappush(queue, num)