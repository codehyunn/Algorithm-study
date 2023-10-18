import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

length = [1 for _ in range(n)]

for i in range(1,n) :
    for j in range(i) :
        if array[i] < array[j] :
            length[i] = max(length[i], length[j]+1)

print(max(length))