from collections import deque

def solution(priorities, location):
    n_process = len(priorities)
    answer = []
    
    priorities = deque(priorities)
    order = deque([i for i in range(n_process)])
        
    while len(answer) < n_process :
        x = priorities.popleft()
        y = order.popleft()
        
        flag = False
        for priority in priorities :
            if priority > x :
                flag = True
                break
        
        if flag :
            priorities.append(x)
            order.append(y)
        
        else :
            answer.append(y)

    return answer.index(location)+1