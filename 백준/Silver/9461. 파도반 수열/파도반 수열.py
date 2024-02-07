import sys  

input = sys.stdin.readline

T = int(input())
testcases = [int(input()) for _ in range(T)]

_max = max(testcases)
pados = [1 for _ in range(_max+1)]

if 3 < _max :
    pados[4] = 2

if 4 < _max :
    pados[5] = 2
    
for i in range(6, _max+1) :
    pados[i] = pados[i-1] + pados[i-5]

for n in testcases :
    print(pados[n])