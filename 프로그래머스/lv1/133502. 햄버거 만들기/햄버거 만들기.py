def solution(ingredient):
    answer = 0
    if len(ingredient) >= 4 :
        i = 4
        while ingredient :
            if ingredient[i-4:i] == [1,2,3,1]:
                del ingredient[i-4:i]
                answer += 1
                i -= 4
            if i == len(ingredient)+1 :
                break
            i += 1
    return answer


