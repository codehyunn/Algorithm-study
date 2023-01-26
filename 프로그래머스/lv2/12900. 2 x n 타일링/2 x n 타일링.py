def solution(n):
    cache = [0]*(n+1)
    if n >= 1 : cache[1] = 1
    if n >= 2 : cache[2] = 2
    if n >= 3 :
        for i in range(3, n+1) :
            cache[i] = (cache[i-1] + cache[i-2]) % 1000000007
    return cache[n] % 1000000007 