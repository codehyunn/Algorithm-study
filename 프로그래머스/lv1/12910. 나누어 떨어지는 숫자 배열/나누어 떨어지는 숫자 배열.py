def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if len(answer) == 0 : 
        answer = [-1]
    return answer