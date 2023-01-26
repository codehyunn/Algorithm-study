from itertools import permutations
def solution(numbers):
    nums = []
    answer = 0
    for i in range(1,len(numbers)+1) :
        nums.extend([int(''.join(x)) for x in permutations(numbers, i) if int(''.join(x))>1])
        nums = list(set(nums))
    
    for n in nums :
        for i in range(2, int(n**(1/2))+1) :
            if n%i == 0 : break
        else :
            answer += 1
    return answer