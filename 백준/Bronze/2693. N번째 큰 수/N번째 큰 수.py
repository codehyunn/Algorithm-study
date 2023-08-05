import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T) :
    A = sorted(list(map(int, input().split())))
    ans.append(A[-3])
    
for a in ans :
    print(a)