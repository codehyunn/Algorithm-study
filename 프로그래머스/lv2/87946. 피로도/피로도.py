from itertools import permutations

def solution(k, dungeons) :
    answer = 0
    count = 0
    tired = k
    
    idxs_list = list(permutations(range(len(dungeons))))
    
    for idxs in idxs_list :
        for i in idxs :
            need, use = dungeons[i]
            if need > tired :
                continue
            tired -= use
            count += 1
            
        answer = max(answer, count)
        tired = k
        count = 0

    return answer