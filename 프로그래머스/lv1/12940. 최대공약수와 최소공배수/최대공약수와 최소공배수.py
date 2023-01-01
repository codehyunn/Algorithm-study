def solution(n, m):
    n,m = (n,m) if n < m else (m,n)
    if m % n == 0 :
        answer = [n,m]
    else :
        for i in range(n-1,0,-1) :
            if n % i == 0 and m % i == 0 :
                x = i
                break
                
        y = ((n//i)*(m//i))*i
        answer = [x,y]
    return answer