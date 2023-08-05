import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

sosu_sum = 0
smallest_sosu = 0

for i in range(M, N+1) :
    if i == 1 :
        continue
    
    sosu = True
    for x in range(2, i) :
        if i % x == 0 :
            sosu = False
            break
        
    if sosu : 
        sosu_sum += i
        if sosu_sum == i :
            smallest_sosu = i

if sosu_sum == 0:
    print(-1)
    
else :
    print(sosu_sum)
    print(smallest_sosu)