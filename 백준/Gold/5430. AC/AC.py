import sys
from collections import deque

input = sys.stdin.readline

def function(funs, nums, xlist) :
    if funs.count('D') > nums : 
        return 'error'
    
    queue = deque(xlist) 
    direction = 0
    
    for f in funs : 
        if not queue :
            return '[]'
                
        if f == 'R' :
            direction += 1
            
        else :
            if direction % 2 == 0 : 
                queue.popleft()
            else :
                queue.pop()
                
    if direction % 2 == 0 :
        return '['+','.join(list(queue))+']'
    else :
        return '['+','.join(list(queue)[::-1])+']'

testcase = int(input())
for t in range(testcase) : 
    p = input().rstrip()
    n = int(input())
    
    input_nums = input().rstrip()[1:-1].split(',')
    xlist = list(input_nums) if n != 0 else []

    print(function(p,n,xlist))