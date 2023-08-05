import sys
input = sys.stdin.readline

a,b = map(int, input().split())

min_num, max_num = min(a,b), max(a,b)
answers = [1, min_num*max_num]

for i in range(min_num, 0, -1) :
    if max_num % i == 0 and min_num % i == 0:
        answers[0] = i
        break
    
if max_num % min_num == 0 :
    answers[1] = max_num
elif answers[0] > 1 :
    answers[1] = answers[0] * (max_num//answers[0]) * (min_num//answers[0])
    
for a in answers :
    print(a)