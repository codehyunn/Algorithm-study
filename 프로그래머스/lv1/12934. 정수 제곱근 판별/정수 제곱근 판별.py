def solution(n):
    answer = 0
    sqrtn = n ** (1/2)
    if sqrtn == int(sqrtn):
        answer = (sqrtn+1)**2 
    else :
        answer = -1
    return answer