def solution(survey, choices):
    result = {0 : {'R' : 0, 'T' : 0}, 1 : {'C' : 0, 'F' : 0},
              2 : {'J' : 0, 'M' : 0}, 3 : {'A' : 0, 'N' : 0}}
    maplist = [['R','T'], ['C','F'],['J','M'],['A','N']]
    answer = ''
    
    for s,c in list(zip(survey, choices)) :
        key1 = maplist.index(sorted(list(s)))
        key2 = s[c//4]
        w = c%4 if c//4 == 1 else 4-c%4
        result[key1][key2] += w
    
    for r in result.items() :
        a = sorted(r[1].items(),reverse=True, key=lambda x : x[1])
        answer += a[0][0]
             
    return answer