def solution(a, b):
    x = abs(a-b) + 1
    if x == 1 :
        answer = a
    elif x % 2 == 0 :
        answer = (a+b) * (x/2)
    else :
        answer = (a+b)//2 * x
        
    return answer