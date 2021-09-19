#1260 DFS와 BFS
from queue import Queue
N,M,V = map(int,input().split())
# N = 정점 개수, M = 간선 개수, V = 시작 정점 번호

adj = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    adj[a-1].append(b) ; adj[b-1].append(a)

for i in range(N):
    adj[i].sort()

adj2 = list(adj) ; visited2 = list(visited)

#dfs
def dfs(v): #v=정점번호 v-1=인덱스
    visited[v-1] = True
    print(v, end = ' ')
    for j in adj[v-1]:
        if not visited[j-1]:
            dfs(j)
    
#bfs
def bfs(v):
    queue = Queue()
    queue.put(v)
    visited2[v-1] = True
    while not (queue.qsize() == 0) :
        v = queue.get()
        print(v, end=' ')
        for j in adj2[v-1]:
            if not visited2[j-1]:
                queue.put(j)
                visited2[j-1] = True

dfs(V)
print('')
bfs(V)
