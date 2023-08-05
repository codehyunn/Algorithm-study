import sys
input = sys.stdin.readline

people = 0
max_people = 0
for _ in range(10) :
    person_out, person_in = map(int, input().split())
    people -= person_out
    people += person_in
    max_people = max(max_people, people)
    
print(max_people)