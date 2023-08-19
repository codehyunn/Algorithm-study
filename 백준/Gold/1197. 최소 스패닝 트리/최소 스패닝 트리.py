import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

vertex, edge = map(int,input().split())

parents = [i for i in range(vertex+1)]
edges = []

for _ in range(edge) :
    a,b,c = map(int, input().split())        
    edges.append((c,a,b))

edges = sorted(edges, key=lambda x:x[0])


def find_root(parents, x) :
    if parents[x] != x :
        parents[x] = find_root(parents, parents[x])
    return parents[x] 
        

def union_root(parents,a,b) :
    if a > b :
        parents[a] = b
    else :
        parents[b] = a
             

answer = 0
for edge in edges :
    cost, a, b = edge
    root_a = find_root(parents, a)
    root_b = find_root(parents, b)
    
    if root_a == root_b :
        continue 
    
    union_root(parents, root_a, root_b)
    answer += cost
    
print(answer)