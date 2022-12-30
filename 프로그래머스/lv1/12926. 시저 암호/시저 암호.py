def solution(s, n):
    s = list(s)
    for i in range(len(s)) :
        if (s[i].isupper()) :
            result = (ord(s[i]) + n - 65) % 26 + 65
            s[i] = chr(int(result))
        elif (s[i].islower()) :
            result = (ord(s[i]) + n - 97) % 26 + 97
            s[i] = chr(int(result))
        else :
            pass
    answer = ''.join(s)
    return answer