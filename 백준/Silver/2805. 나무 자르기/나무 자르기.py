import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = sorted(list(map(int,input().split())), reverse=True)

start, end = 0, max(trees)
answer = 0

while start <= end :
    home = 0
    mid = (start+end)//2
    
    for tree in trees :
        if tree > mid :
            home += (tree-mid)
        else :
            break
    
    if home < m :
        end = mid - 1
    else :
        answer = mid
        start = mid + 1
        
print(answer)