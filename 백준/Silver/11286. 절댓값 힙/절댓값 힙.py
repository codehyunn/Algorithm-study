import sys 
import heapq 
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
queue = []
nums_in_queue = defaultdict(int)

for _ in range(n) :
    x = int(input())
    if x != 0 : 
        nums_in_queue[x] += 1
        if x < 0 : 
            heapq.heappush(queue, -x)
        else : 
            heapq.heappush(queue, x)
            
    else :
        if not queue :
            print(0)
        else :
            out = heapq.heappop(queue)
            if nums_in_queue[-out] :
                out = -out
                
            nums_in_queue[out] -= 1
            if nums_in_queue[out] == 0 :
                nums_in_queue.pop(out)
            
            print(out)