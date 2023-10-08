import sys
from collections import defaultdict

input = sys.stdin.readline

def main(n, people) :
    count = defaultdict(int)
    last = defaultdict(int)
    for idx, p in enumerate(people) :
        count[p] += 1
        last[p] = idx + 1
    
    curr_position, answer = 0, 0
    for group, last_position in sorted(last.items(), key = lambda x : x[1]) :
        curr_position += count[group]
        if last_position > curr_position :
            answer += (last_position-curr_position)*count[group]*5
    
    print(answer)

cases = int(input())
cases_info = []

for _ in range(cases) :
    n = int(input())
    people = list(map(str, list(input().rstrip())))
    cases_info.append((n,people))

for (n, people) in cases_info :
    main(n,people) 