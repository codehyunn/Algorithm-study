from itertools import *

def solution(nums):
    answer = 0
    comb = list(combinations(nums,3))
    for c in comb :
        flag = True
        for i in range(2,sum(c)):
            if sum(c) % i == 0 :
                flag = False
                break
        if flag :
            answer += 1
        
    return answer