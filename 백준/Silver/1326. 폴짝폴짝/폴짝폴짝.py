import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))
a,b = map(int, input().split())

jump = [-1] * (N+1)
queue = deque([a])
jump[a] = 0

while queue :
    v = queue.popleft()
    for i in range(v, N+1, nums[v]) :
        if jump[i] < 0 :
            queue.append(i)
            jump[i] = jump[v] + 1
        if i == b :
            print(jump[i])
            exit(0)
            
    for j in range(v, 0, -nums[v]) :
        if jump[j] < 0 :
            queue.append(j)
            jump[j] = jump[v] + 1
        if j == b :
            print(jump[j])
            exit(0)

print(-1)