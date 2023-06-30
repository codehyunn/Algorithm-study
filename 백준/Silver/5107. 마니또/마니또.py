import sys

def dfs(connect_dict, v, visited, cnt) :
    x = connect_dict[v]
    if not visited[x] :
        visited[x] = True
        v = x
        return dfs(connect_dict, v, visited, cnt+1)
    else :
        return cnt
        
input = sys.stdin.readline

case = 1
while True : 
    N = int(input())
    if N == 0 :
        break
    
    connect_dict = dict()
    names_dict = dict()
    name_int = 0
    
    for i in range(N) :
        a,b = input().split()
        if a not in names_dict :
            names_dict[a] = name_int
            name_int += 1
        if b not in names_dict :
            names_dict[b] = name_int
            name_int += 1
        connect_dict[names_dict[a]] = names_dict[b]
    
    visited = [False] * N
    connect_cnt = 0
    
    for i in range(N) :
        if visited[i] :
            continue  
        visited[i] = True
        is_finished = dfs(connect_dict, i, visited, 0)
        if is_finished > 0 :
            connect_cnt += 1
            
    print(case, connect_cnt)
    case += 1