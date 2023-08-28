import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n) :
    row = list(input().strip())
    graph.append(row)

def check_count(graph, r, c) :
    answer, row_count, column_count = 1, 1, 1

    for i in range(n) :
        for j in range(n-1) :
            if graph[j][i] == graph[j+1][i] :
                column_count += 1
            else :
                answer = max(answer, column_count)
                column_count = 1
                
            if graph[i][j] == graph[i][j+1] :
                row_count += 1
            else :
                answer = max(answer, row_count)
                row_count = 1
        answer = max(answer, row_count, column_count)
        row_count, column_count = 1, 1
        
    return answer 


answer = 1
dr, dc = [1,-1,0,0], [0,0,1,-1]
for r in range(n) :
    for c in range(n) :
        for i in range(4) :
            sr, sc = r+dr[i], c+dc[i]
            if 0<=sr<n and 0<=sc<n and graph[r][c] != graph[sr][sc]:
                graph[sr][sc], graph[r][c] = graph[r][c], graph[sr][sc]
                answer = max(answer, check_count(graph, r, c))
                graph[sr][sc], graph[r][c] = graph[r][c], graph[sr][sc]
                
        
print(answer)