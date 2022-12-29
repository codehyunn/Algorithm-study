def solution(left, right):
    nums = [i for i in range(left, right+1)]
    answer = sum([-x if x**(1/2) == int(x**(1/2)) else x for x in nums])
    return answer