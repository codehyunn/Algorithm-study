import sys
#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

T = int(input())
answers  = [[0 for _ in range(4)] for _ in range(T)]

quarter = 25
dime = 10
nickel = 5
penny = 1
    
for i in range(T) :
    C = int(input())

    if C >= quarter :
        answers[i][0] = C//quarter
        C %= quarter
    
    if C >= dime :
        answers[i][1] = C//dime
        C %= dime
        
    if C >= nickel :
        answers[i][2] = C//nickel
        C %= nickel
    
    if C >= penny :
        answers[i][3] = C//penny
        C %= penny
    
for answer in answers :
    print(*answer)