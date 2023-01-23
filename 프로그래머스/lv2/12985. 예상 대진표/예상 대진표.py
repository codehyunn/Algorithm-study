import math
def solution(n,a,b):
    answer = 0
    a, b = a-1, b-1
    for i in range(int(math.log2(n))) :
        if a != b :
            answer += 1
            a,b = a//2, b//2
        else :
            break
    return answer