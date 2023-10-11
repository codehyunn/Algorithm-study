import sys
input = sys.stdin.readline

n,k = map(int, input().split())
    
if n <= k :
    print(0)
    exit()

answer, bottle = 0, n
while True :
    n = bottle
    
    binary = ''
    while n > 1 :
        n, x = divmod(n, 2)
        binary += str(x)
    binary += '1'
    
    if binary.count('1') <= k :
        print(answer)
        exit()
        
    idx = binary.find('1')
    answer += 2**idx
    bottle += 2**idx