def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        tmp = []
        for x in range(n) :
            tmp.append((arr1[i]%2) or (arr2[i]%2))
            arr1[i] //= 2
            arr2[i] //= 2
        answer.append(''.join(['#' if t == 1 else ' ' for t in tmp[::-1]]))   
    return answer