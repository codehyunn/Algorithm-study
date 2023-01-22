def solution(n):
    cnt_n = bin(n)[2:].count('1')
    answer = n + 1
    while True :
        if bin(answer)[2:].count('1') == cnt_n :
            break
        answer += 1
    return answer