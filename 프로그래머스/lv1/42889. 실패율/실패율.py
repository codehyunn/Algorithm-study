from collections import Counter
def solution(N, stages):
    count = [0] * N
    total = len(stages)
    for key, value in sorted(Counter(stages).items(), key=lambda x: x[0]):
        if key-1 < N : 
            count[key-1] = value/total
            total -= value
    answer = sorted(range(1,N+1), reverse=True, key=lambda x : count[x-1])
    return answer