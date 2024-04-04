def solution(numbers, target) :
    global answer 
    answer = 0

    dfs(numbers, target, 0, 0, numbers[0])
    dfs(numbers, target, 0, 1, -numbers[0])
    
    return answer


def dfs(numbers, target, x, op, _sum) :
    global answer 
    if x == len(numbers)-1 :
        if _sum == target :
            answer += 1
        return
    
    ops = {0:-1, 1:1}
    for i in range(2) :
        dfs(numbers, target, x+1, i, _sum+numbers[x+1]*ops[i])
   