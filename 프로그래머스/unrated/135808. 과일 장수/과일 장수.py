def solution(k, m, score):
    score = sorted(score)[len(score)%m:]
    answer = 0
    for i in range(len(score)//m) :
        answer += m*min(score[m*i : m*(i+1)])
    return answer