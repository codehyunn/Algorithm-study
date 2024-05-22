from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    
    # 작업이 필요한 날 계산
    for progress, speed in zip(progresses, speeds) :
        days, half = divmod(100-progress, speed)
        if half :
            days += 1
        queue.append(days)
    
    # 배포될 작업 수 계산
    prev = queue.popleft()
    answer.append(1)
    
    while queue :
        now = queue.popleft()
        if prev >= now :
            answer[-1] += 1
        else :
            answer.append(1)
            prev = now
        
    return answer