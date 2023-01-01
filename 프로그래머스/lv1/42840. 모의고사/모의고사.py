def solution(answers):
    pattern = ['12345','21232425','3311224455']
    resultdict = dict()
    answer = list()

    q = len(answers)
    for i,p in enumerate(pattern) :
        ans = list(map(int,((q//len(p))*p+p[:q%len(p)])))
        resultdict[i+1] = sum([1 for x,y in zip(ans,answers) if x == y])

    maxresult = max(resultdict.values())
    for key,value in resultdict.items() :
        if value == maxresult :
            answer.append(key)
    
    return sorted(answer)