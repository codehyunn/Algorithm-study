def solution(s):
    s = list(s.lower())
    check = True
    for i in range(len(s)) :
        if s[i].isspace():
            check = True
        if check :
            if s[i].isalpha():
                s[i] = s[i].upper()
                check = False
            elif s[i].isdigit() :
                check = False
    answer = ''.join(s)
    return answer