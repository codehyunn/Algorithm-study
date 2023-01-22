def solution(brown, yellow):
    plus = brown//2 + 2 
    multi = brown + yellow
    
    x,y = 0,0
    for i in range(1, plus//2+1) :
        if i * (plus-i) == multi :
            x, y = i, plus - i
            break
            
    return [x,y] if x >= y else [y,x]