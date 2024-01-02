import sys

input = sys.stdin.readline

N = int(input()) # 도시의 수
M = int(input()) # 여행 계획에 속한 도시의 수

def union(x,y,parents) :
    x, y = find(x, parents), find(y, parents)
    if x > y :
        parents[x] = y
    else :
        parents[y] = x
    
def find(x, parents) : 
    if x != parents[x] :
        parents[x] = find(parents[x], parents)
    return parents[x]

parents = [i for i in range(N+1)]
for i in range(N) :
    link_info = list(map(int, input().split()))
    for j in range(N) :
        if link_info[j] == 1 :
            union(i+1,j+1,parents)

plan = list(map(int, input().split()))

crit = parents[plan[0]]
for x in plan[1:] :
    if crit != parents[x] :
        print('NO')
        exit()
print('YES')