def solution(number, limit, power):
    answer = 0
    nums = []
    
    for n in range(1,number+1) :
        cnt = 0
        for i in range(1,int(n**0.5)+1) :
            if i == int(n**0.5) and int(n**0.5) == n**0.5 :
                cnt += 1
                continue
            if n%i == 0 :
                cnt += 2
                
        if cnt > limit :
            cnt = power
        nums.append(cnt)
        
    answer = sum(nums)
    return answer