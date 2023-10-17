import sys

input = sys.stdin.readline

N = int(input())
schedule = [[0,0]]+[list(map(int,input().split())) for _ in range(N)]

cache = [0 for _ in range(N+1)]

for i in range(1, N+1) :
    day, money = schedule[i]
    if i+day-1 <= N :
        cache[i+day-1] = max(cache[i+day-1], max(cache[:i])+money)
    
print(max(cache))