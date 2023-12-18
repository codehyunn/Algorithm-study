import sys

input = sys.stdin.readline
n,m = map(int,input().split())

roads = []
for _ in range(m) :
    a,b,cost = map(int, input().split())
    roads.append((cost,a,b))

roads.sort()

def find_parent(parents, x) :
    if parents[x] != x :
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, a, b) :
    a, b = parents[a], parents[b]
    if a > b:
        parents[a] = b
    else :
        parents[b] = a

total_cost, last_cost = 0, 0
parents = [i for i in range(n+1)]

for cost,a,b in roads : 
    if find_parent(parents, a) != find_parent(parents, b) :
        union(parents, a, b)
        total_cost += cost
        last_cost = cost
        
print(total_cost-last_cost)