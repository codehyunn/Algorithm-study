def solution(n):
    answer = [0]*(n+1)
    if n>=1 : answer[1] = 1
    if n>=2 : answer[2] = 2
    if n>=3 :
        for i in range(3, n+1) :
            answer[i] = answer[i-1] + answer[i-2] 
    return answer[n]%1234567
