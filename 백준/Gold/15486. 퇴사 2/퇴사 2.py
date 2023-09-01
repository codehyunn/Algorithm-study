import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n = int(input())
data = [[0,0]]

for i in range(n) :
    t, p = map(int, input().split())
    data.append([t,p])

cost = [0 for _ in range(n+1)]

for i in range(1, n+1) :
    t, p = data[i]
    fin_day = i+t-1
    
    cost[i] = max(cost[i], cost[i-1])

    if fin_day > n :
        continue
    
    cost[fin_day] = max(cost[fin_day], cost[fin_day-1], p+cost[i-1])
    
print(cost[-1])