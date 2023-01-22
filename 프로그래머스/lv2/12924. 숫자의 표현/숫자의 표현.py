def solution(n):
    nums_list = [0] * (n//2+2)
    answer = 0
    same = False
    
    for i in range (1, len(nums_list)) :
        for j in range(i, i + n//i) :
            nums_list[i] += j
            if nums_list[i] == n :
                answer += 1
                if i == n :
                    same = True
                break
                
    if not same :
        answer += 1
            
    return answer