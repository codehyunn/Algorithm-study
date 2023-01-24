def solution(n, money):
    cache = [0] * (n+1)
    money = sorted(money)
    for m in money :
        cache[m] += 1
        for i in range(m+1, n+1) :
            cache[i] += cache[i-m]
    return cache[n]