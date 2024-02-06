import sys  
import heapq 

input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n) :
    inp = int(input())
    if inp == 0 :
        if not queue :
            print(0)
        else : 
            out = heapq.heappop(queue)
            print(-out)
    else :
        heapq.heappush(queue, -inp)