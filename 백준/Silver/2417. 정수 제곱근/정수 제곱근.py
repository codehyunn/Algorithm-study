import sys
input = sys.stdin.readline
N = int(input())

start = 0
end = N

while start <= end : 
    mid = (start+end)//2
    if N <= mid**2 :
        end = mid - 1
    else :
        start = mid + 1
    
print(start)
    