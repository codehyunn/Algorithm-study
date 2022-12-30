def solution(d, budget):
    d = sorted(d)
    cnt, dsum =0, 0
    for i in d :
        if budget >= dsum+i :
            cnt += 1
            dsum += i
        else :
            break
    return cnt