import sys
input = sys.stdin.readline

a,b = map(int, input().split())

def _sum(x) :
    return (x*(x+1)*(2*x+1))//6

def _count(x) :
    return (x*(x+1))//2

def calculate(x) :
    for i in range(1, x+1) :
        count = _count(i)
        if count >= x :
            return _sum(i) - (i*(count-x))
    return 0

ans = calculate(b) - calculate(a-1)
    
print(ans)