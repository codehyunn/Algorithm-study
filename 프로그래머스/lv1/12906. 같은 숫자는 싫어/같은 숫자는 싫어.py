from collections import deque
def solution(arr):
    arr = deque(arr)
    tmp = arr.popleft()
    answer = [tmp]
    while len(arr) > 0 :
        num = arr.popleft()
        if tmp != num :
            answer.append(num)
            tmp = num
    return answer