def solution(n, lost, reserve):
    stds = [1 for _ in range(n)]
    for i in lost : stds[i-1] -= 1
    for j in reserve : stds[j-1] += 1
    
    if stds[0] > 1 and stds[1] < 1 :
        stds[0] -= 1
        stds[1] += 1
    elif stds[-1] > 1 and stds[-2] < 1 :
        stds[-1] -= 1
        stds[-2] += 1
        
    for i in range(1,n-1) :
        if stds[i] > 1 :
            if stds[i-1] < 1  :
                stds[i] -= 1
                stds[i-1] += 1
            elif stds[i+1] < 1 :
                stds[i] -= 1
                stds[i+1] += 1
                
    return len([x for x in stds if x>=1])