import sys

input = sys.stdin.readline
n,m = map(int,input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))
    
block_shapes = [((0,1),(0,2),(0,-1)), ((1,0),(2,0),(-1,0)),
                ((0,1),(1,0),(1,1)),
                ((-1,0),(-2,0),(0,1)),((-1,0),(-2,0),(0,-1)),((1,0),(2,0),(0,1)),((1,0),(2,0),(0,-1)),
                ((0,1),(0,2),(1,0)),((0,1),(0,2),(-1,0)),((0,-1),(0,-2),(1,0)),((0,-1),(0,-2),(-1,0)),
                ((-1,0),(-1,-1),(-1,1)),((1,0),(1,-1),(1,1)),((0,-1),(-1,-1),(1,-1)),((0,1),(1,1),(-1,1)),
                ((0,-1),(-1,-1),(1,0)),((0,1),(-1,1),(1,0)),((0,1),(1,0),(1,-1)),((0,-1),(1,0),(1,1))]

check = [1,-1,2,-2]
answer = 0

for x in range(n):
    for y in range(m):
        no_x, no_y = [],[]
        for c in check :
            if x+c<0 or x+c>=n :
                no_x.append(c)
            if y+c<0 or y+c>=m :
                no_y.append(c)
        
        for (a,b,c) in block_shapes :
            (ax,ay), (bx,by), (cx,cy) = a,b,c
            if ax in no_x or bx in no_x or cx in no_x :
                continue
            if ay in no_y or by in no_y or cy in no_y :
                continue
            
            answer = max(answer, graph[x][y]+graph[x+ax][y+ay]+graph[x+bx][y+by]+graph[x+cx][y+cy])
            
print(answer)