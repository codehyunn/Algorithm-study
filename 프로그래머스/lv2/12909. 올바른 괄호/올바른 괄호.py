def solution(s):
    cnt = 0
    for b in s :
        if b == '(' :
            cnt += 1
        elif cnt > 0:
            cnt -= 1
        else :
            return False

    return cnt == 0