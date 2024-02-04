import sys 
import heapq
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    min_queue, max_queue = [], []
    nums_in_queue = defaultdict(int)
    
    k = int(input())
    for _ in range(k) :
        op, num = input().split()
        num = int(num)
        
        if op == 'I' : 
            heapq.heappush(min_queue, num)
            heapq.heappush(max_queue, -num)
            nums_in_queue[num] += 1
        
        if op == 'D' :
            if not nums_in_queue :
                continue
            
            if num == -1 :
                while True : 
                    x = heapq.heappop(min_queue)
                    if x in nums_in_queue :
                        nums_in_queue[x] -= 1
                        if nums_in_queue[x] == 0 :
                            nums_in_queue.pop(x)
                        break

            else :
                while True :
                    x = heapq.heappop(max_queue)
                    if -x in nums_in_queue :
                        nums_in_queue[-x] -= 1
                        if nums_in_queue[-x] == 0 :
                            nums_in_queue.pop(-x)
                        break

    if not nums_in_queue :
        print('EMPTY')
    else :
        print(max(nums_in_queue), min(nums_in_queue))