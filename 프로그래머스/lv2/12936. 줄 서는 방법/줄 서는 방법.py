def solution(n, k):
    answer = []
    people = list(range(1,n+1))
    
    factorial = [1]*(n)
    for i in range(2, n) :
        factorial[i] = factorial[i-1] * i

    while n > 0 :
        answer.append(people.pop((k-1)//factorial[n-1]))
        k %= factorial[n-1]
        n -= 1
        
    return answer