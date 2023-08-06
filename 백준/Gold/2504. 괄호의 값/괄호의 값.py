import sys
input = sys.stdin.readline

string = list(input().strip())

pair = {'(':')', ')':'(', '[':']', ']':'['}
score = {'[':3, ']':3, '(':2, ')':2}

check = []
temp, answer = 1, 0
close_before = False

for s in string :
    if s == '(' or s == '[' :
        check.append(s)
        temp *= score[s]
        close_before = False
        
    else : 
        if check and check[-1] == pair[s] :
            check.pop()
            
            if close_before :
                temp //= score[s]
                continue
            
            answer += temp
            temp //= score[s]
                            
        else :
            print(0)
            exit(0)
        
        close_before = True

if check :
    print(0)
    exit(0)
            
print(answer)