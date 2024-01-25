import sys

input = sys.stdin.readline

m = int(input())

S = set()

for i in range(m) :
    oper = input().rstrip()
    if oper[-1].isdigit() :
        oper, x = oper.split()
        x = int(x)
    
    if oper == 'all' :
        S.update([i for i in range(1,21)]) 
        
    elif oper == 'empty' :
        S = set()
        
    elif oper == 'add' :
        S.add(x)
        
    elif oper == 'remove' :
        if x in S :
            S.remove(x)
        
    elif oper == 'check' :
        if x in S :
            print(1)
        else :
            print(0)
            
    elif oper == 'toggle' :
        if x in S :
            S.remove(x)
        else :
            S.add(x)    