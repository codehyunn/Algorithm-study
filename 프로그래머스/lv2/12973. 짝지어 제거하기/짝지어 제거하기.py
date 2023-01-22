def solution(s):
    if len(s) % 2 == 1 : 
        return 0
    
    string = []
    for i in s :
        string.append(i)
        if len(string) >= 2 and string[-2] == string[-1] :
            string.pop()
            string.pop()
    
    if string :
        return 0
    else :
        return 1