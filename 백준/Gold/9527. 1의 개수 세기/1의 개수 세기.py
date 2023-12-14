import sys

#sys.stdin = open('./answer.txt', 'r')
input = sys.stdin.readline

numlist = [0] * 55
for i in range(1, 55) :
    numlist[i] = numlist[i-1]*2 + 2**(i-1)

a,b = map(int, input().split())

def calculate(x) :
    result = 0
    num = x
    binx = bin(x)[2:]
    
    for i in range(len(binx)) :
        idx = len(binx)-i-1
        if binx[i] == '1' :
            result += numlist[idx]
            result += num-2**idx+1
            num -= 2**idx
                                
    return result

print(calculate(b)-calculate(a-1))
