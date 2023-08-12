import sys
import heapq

input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n) :
    heapq.heappush(cards, int(input()))

if n == 1 :
    print(0)
    exit()

answer = 0     
while len(cards) > 1 :
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    
    answer += (a+b)
    heapq.heappush(cards, a+b)
     
print(answer)