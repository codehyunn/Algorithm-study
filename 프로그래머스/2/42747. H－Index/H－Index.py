def solution(citations):
    citations = sorted(citations,reverse=True)
    point = 0
    
    for h in range(citations[0], -1, -1) :
        if point+1 < len(citations) and citations[point+1] >= h :
            point += 1
            
        if point+1 >= h :
            return h
        
        
        