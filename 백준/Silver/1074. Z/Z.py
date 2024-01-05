import sys

input = sys.stdin.readline

n,r,c = map(int,input().split())

crit = 2 ** n
ans = 0

for i in range(n-1, -1, -1) :
    crit //= 2 
    if r < crit :
        if c < crit :
            ans += 0
        else :
            ans += crit*crit
            c -= crit
    else :
        r -= crit
        if c < crit :
            ans += crit*crit*2
        else :
            ans += crit*crit*3
            c -= crit
    
print(ans)