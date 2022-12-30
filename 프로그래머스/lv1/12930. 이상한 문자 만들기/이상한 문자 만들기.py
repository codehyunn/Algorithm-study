def solution(s):
    idx = 0
    s = list(s.lower())
    for i in range(len(s)) :
        if s[i] == ' ':
            idx = -1
        if idx % 2 == 0 :
            s[i] = s[i].upper()
        idx += 1
    answer = ''.join(s)
    return answer