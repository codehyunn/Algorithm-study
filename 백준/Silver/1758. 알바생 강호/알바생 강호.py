import sys 

input = sys.stdin.readline

N = int(input())
people = [int(input()) for _ in range(N)]
people.sort(reverse=True)

total_tip = 0
for order, tip in enumerate(people) :
    if tip-order > 0 :
        total_tip += (tip-order)

print(total_tip)