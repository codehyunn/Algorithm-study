import sys

input = sys.stdin.readline
N = int(input())

start, end = 0, N
while start <= end : 
    mid = (start+end)//2
    if mid**2 < N :
        start = mid+1
    elif N < mid**2 :
        end = mid-1
    else :
        print(mid)
        break