def solution(lottos, win_nums):
    ranking = [6,6,5,4,3,2,1]
    
    zeros = lottos.count(0)
    for i in range(zeros) :
        lottos.remove(0)
        
    match = 0
    for lotto in lottos:
        if lotto in win_nums :
            match += 1
    
    answer = [ranking[match+zeros], ranking[match]]
    return answer