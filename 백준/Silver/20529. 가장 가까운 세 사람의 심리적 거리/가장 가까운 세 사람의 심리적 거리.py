import sys  
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline

t = int(input())

def count(x,y) :
    ans = 0
    for i in range(4) :
        if x[i] != y[i] :
            ans += 1
    return ans

for _ in range(t) :
    n = int(input())

    mbti = defaultdict(int)
    people = list(input().split())
    
    answer = 12
    finish = False
    for p in people :
        mbti[p] += 1
        if mbti[p] == 3 :
            answer = 0
            finish = True
    
    if not finish :
        if len(mbti) < 3 :
            a,b = mbti.keys()
            answer = min(answer, 2*count(a,b))
                
        else :
            for a,b,c in list(combinations(mbti.keys(), 3)) :
                ab,bc,ca = count(a,b), count(b,c), count(c,a)
                answer = min(answer, ab+bc+ca)
                
                if mbti[a] == 2 :
                    answer = min(answer, 2*ab, 2*ca)
                
                if mbti[b] == 2 :
                    answer = min(answer, 2*bc, 2*ab)
                
                if mbti[c] == 2 :
                    answer = min(answer, 2*ca, 2*bc) 
        
    print(answer)