import sys
import heapq

input = sys.stdin.readline
N = int(input())

numbers = [] 
for i in range(N) :
    numbers.append(list(map(int, input().split())))

heap = numbers[0]
heapq.heapify(heap)

for number in numbers[1:] :
    for n in number :
        if heap[0] < n :
            heapq.heappop(heap)
            heapq.heappush(heap, n)
        
print(heapq.heappop(heap))