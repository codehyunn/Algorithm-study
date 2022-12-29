def solution(s):
    p = [1 for i in s if i in ['p', 'P']]
    y = [1 for j in s if j in ['y', 'Y']]
    
    return sum(p) == sum(y)