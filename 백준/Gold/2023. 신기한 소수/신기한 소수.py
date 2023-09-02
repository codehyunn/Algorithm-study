import sys 

input = sys.stdin.readline

n = int(input())

def sosu(x, length) :
    global nums
    
    if length == n+1 :
        return 
    
    for i in range(2, int(x**(1/2)+1)) :
        if x % i == 0 :
            return  
    
    if x >= 10**(n-1) :
        nums.append(x)
        
    for i in range(1,10) :
        sosu(10*x+i, length+1)

nums = []
for i in range(2,10) :
    sosu(i, 1)        

for num in nums :
    print(num)