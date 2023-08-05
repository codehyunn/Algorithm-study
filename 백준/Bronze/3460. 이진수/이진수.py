import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    n = int(input())
    
    binary = []
    while n > 1 :
        binary.append(n%2)
        n //= 2
    binary.append(n)
        
    for idx, b in enumerate(binary) :
        if b == 1 :
            print(idx, end=' ')