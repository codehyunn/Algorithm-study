from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people :
        if len(people) > 1 and people[-1]+people[0] <= limit :
            people.popleft()
            people.pop()
        else :
            people.pop()
        answer += 1
    return answer