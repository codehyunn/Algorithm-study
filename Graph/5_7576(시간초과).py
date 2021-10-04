m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(q):
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    cnt = 0
    while q!=[]:
        clist = []
        for j in range(len(q)) :
            v = q.pop(0)
            for i in range(4) :
                x,y = v[0]+dx[i],v[1]+dy[i]
                if n>x>=0 and m>y>=0 and tomato[x][y] == 0 and not visited[x][y]:
                    clist.append([x,y])
                    visited[x][y] = True
                    tomato[x][y] = 1
        if clist == []:
            break
        else:
            q = clist
            cnt += 1
    return cnt

q=[]
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1 :
            q.append([i,j])

cnt = bfs(q)
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0 :
            cnt = -1
    
print(cnt)
