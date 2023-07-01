import sys

input = sys.stdin.readline
N = int(input())

start, end = 0, N
while start <= end : 
    mid = (start+end)//2
    if N//mid < mid : 
        end = mid-1
    elif mid < N//mid :
        start = mid+1
    else :
        if N%mid == 0 :
            print(mid)
            break
        end = mid-1    
        