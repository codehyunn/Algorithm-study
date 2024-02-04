import sys 
from collections import defaultdict

input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    n = int(input())
    closet = defaultdict(int)
    
    for _ in range(n) : 
        _, category = input().split()
        closet[category] += 1    
    
    answer = 1
    for cloth in closet.values() :
        answer *= (cloth+1)

    print(answer-1)