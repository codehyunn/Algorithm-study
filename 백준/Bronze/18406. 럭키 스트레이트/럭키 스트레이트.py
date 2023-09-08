import sys
input = sys.stdin.readline

n = input().rstrip()
half_length = len(n)//2

_sum = [0,0]
for i in range(2) :
    for j in range(half_length) :
        idx = half_length*i + j
        _sum[i] += int(n[idx])
        
if _sum[0] == _sum[1] :
    print('LUCKY')
else :
    print('READY')