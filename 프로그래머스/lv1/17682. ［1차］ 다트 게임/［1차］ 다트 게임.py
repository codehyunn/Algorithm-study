def solution(dartResult):
    scores = {'S':1, 'D':2, 'T':3}
    results = []
    
    start = 0
    for i in range(len(dartResult)):
        if not dartResult[i].isdigit() :
            if dartResult[i] == '*' :
                results[-2:] = [2*x for x in results[-2:]]
                start += 1
            elif dartResult[i] == '#' :
                results[-1] = results[-1] * -1
                start += 1
            else :
                result = int(dartResult[start:i]) ** scores[dartResult[i]]
                results.append(result)
                start = i+1
                
    answer = sum(results)
    return answer