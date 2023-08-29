import sys 

input = sys.stdin.readline

N = int(input())

if N < 10 :
    print(N)
    exit(0)

idx = 9
numlist = [[0,1,2,3,4,5,6,7,8,9]]

while idx < N :
    nums = numlist[-1]
    new_nums = []
    for i in range(10) :
        for n in nums :
            if n%10 > i :
                new_nums.append(n*10+i)
    
    idx += len(new_nums)
    numlist.append(sorted(new_nums))
    
    if new_nums[-1] == 9876543210 and idx < N : 
        print(-1)
        exit(0)

print(numlist[-1][N-idx-1])