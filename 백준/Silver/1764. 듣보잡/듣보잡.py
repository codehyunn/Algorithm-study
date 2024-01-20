import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

people_dict = defaultdict(int)
for _ in range(n) :
    people_dict[input().rstrip()] += 1
for _ in range(m) :
    people_dict[input().rstrip()] += 1

answer_list = []
for key, count in sorted(people_dict.items()) :
    if count == 2 :
        answer_list.append(key)
        
print(len(answer_list))
for ans in answer_list :
    print(ans)