import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

m,n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

dx, dy = [1,-1,0,0], [0,0,1,-1]
dp = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

def dfs(x, y) :
    if x == m-1 and y == n-1 :
        return 1 
    
    if visited[x][y] :
        return dp[x][y]
    
    for i in range(4) :
        sx, sy = x+dx[i], y+dy[i]
        if 0<=sx<m and 0<=sy<n and maps[x][y] > maps[sx][sy] :
            dp[x][y] += dfs(sx,sy)
            
    visited[x][y] = True
    return dp[x][y]
            
print(dfs(0,0))