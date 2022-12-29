def solution(arr):
    answer = [-1]
    arr.remove(min(arr))
    if len(arr) > 0 : 
        answer = arr
    return answer