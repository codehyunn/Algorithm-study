import sys
import heapq

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n = int(input())

queue = []
for i in range(n) :
    t,p = map(int, input().split())
    heapq.heappush(queue, (i+t, i+1, p))
    
cost = [[0,0] for _ in range(n+1)]

for i in range(1,n+1) :
    cost[i][0] = max(cost[i-1])
    
    while queue :
        if queue[0][0] != i :
            break
        _, start, money = heapq.heappop(queue)
        cost[i][1] = max(cost[i][1], cost[start][0]+money)
 
print(max(cost[-1]))