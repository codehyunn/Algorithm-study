from collections import deque
def solution(operations):
    answer = deque([])
    for i in operations :
        if i[0] == 'I':
            answer.append(int(i[2:]))
        elif answer and i == "D 1" :
            answer.remove(max(answer))
        elif answer and i == "D -1":
            answer.remove(min(answer))
    if not answer : return [0,0]
    else : return [max(answer), min(answer)]