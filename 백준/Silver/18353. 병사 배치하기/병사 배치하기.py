import sys

input = sys.stdin.readline

N = int(input())
powers = [10000000] + list(map(int,input().split()))

cache = [0] * (N+1)

for i in range(1,N+1) :
    count = 1
    for j in range(1,i) :
        if powers[i] < powers[j] :
            count = max(count, cache[j]+1)
    cache[i] = count
    
print(N-max(cache))