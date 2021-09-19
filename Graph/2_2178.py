#2178 미로탐색

#input, set
N,M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[False for _ in range(M+2)] for _ in range(N+2)]

graph.append([0 for _ in range(M)]) ; graph.insert(0,[0 for _ in range(M)])
for i in range(len(graph)):
    graph[i].append(0) ; graph[i].insert(0,0)

#시작[x,y] 끝[N,M]
def bfs(graph,x,y,N,M) :
    cnt = 1
    queue = [[x,y]]
    visited[x][y] = True
    while queue:
        clist = []
        for i in range(len(queue)) :
            a = queue[0][0] ; b = queue[0][1]
            queue.pop(0)
            if graph[a-1][b] == 1 and not visited[a-1][b] : #up
                clist.append([a-1,b])
                visited[a-1][b] = True
            if graph[a+1][b] == 1 and not visited[a+1][b] : #down
                clist.append([a+1,b])
                visited[a+1][b] = True
            if graph[a][b+1] == 1 and not visited[a][b+1] : #left
                clist.append([a,b+1])
                visited[a][b+1] = True
            if graph[a][b-1] == 1 and not visited[a][b-1] : #right
                clist.append([a,b-1])
                visited[a][b-1] = True
                print(graph[a][b-1])
            
        queue = clist
        cnt += 1
        for i in clist:
            if i == [N,M]:
                return cnt

print(bfs(graph,1,1,N,M))
