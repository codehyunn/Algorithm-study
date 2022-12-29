def solution(s):
    if len(s) != 4 and len(s) != 6 :
        return False
    
    cnt = [1 if i <"A" else 0 for i in s].count(1)
    if cnt == len(s) :
        return True
    else :
        return False