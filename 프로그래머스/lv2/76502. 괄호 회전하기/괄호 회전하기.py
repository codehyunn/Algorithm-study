from collections import deque

def solution(s):
    s = deque(s)
    brackets = {'[':(0,']'), ']':(1,'['), 
                '{':(0,'}'), '}':(1,'{'), 
                '(':(0,')'), ')':(1,'(')}
    
    if len(s)%2 == 1: return 0
    
    answer = 0
    for i in range(len(s)) :
        temp = s.popleft()
        s.append(temp)

        if brackets[s[0]][0] == 1 :
            continue
        
        correct = True 
        stack = []
        for j in s :
            x, pair = brackets[j]
            
            if x == 0:
                stack.append(j)
            elif x == 1 :
                if stack and (pair==stack[-1]) :
                    stack.pop()
                else :
                    correct = False
                    break
            
        if correct : answer += 1
                
    return answer