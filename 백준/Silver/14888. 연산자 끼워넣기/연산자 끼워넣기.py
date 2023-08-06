import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))
operator = list(map(int, input().split()))

operator_list = []
for idx, op in enumerate(operator) :
    operator_list.extend([idx]*op)

max_ans = float('-inf')
min_ans = float('inf')
permutation_list = set(permutations(operator_list))

for i in permutation_list :
    ans = numlist[0] 
    for idx, j in enumerate(i) :
        if j == 0 :
            ans += numlist[idx+1]
        elif j == 1 :
            ans -= numlist[idx+1]
        elif j == 2 :
            ans *= numlist[idx+1]
        else :
            if ans < 0 :
                ans = ((-1*ans)//numlist[idx+1]) * -1
            else :
                ans //= numlist[idx+1]
    if ans > max_ans :
        max_ans = ans
    if ans < min_ans :
        min_ans = ans
            
print(max_ans)
print(min_ans)
