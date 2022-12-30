def solution(s):
    numdict = dict([['zero',0], ['one',1], ['two',2], ['three',3],
                   ['four',4], ['five',5], ['six',6], ['seven',7],
                   ['eight',8], ['nine',9]])
    
    if s.isdigit() :
        return int(s)
    
    else :
        answer, tmp = '',''
        for w in s :
            if w.isdigit() :
                answer += w
            else :
                tmp += w
                if tmp in numdict :
                    answer += str(numdict[tmp])
                    tmp = ''
        return int(answer)