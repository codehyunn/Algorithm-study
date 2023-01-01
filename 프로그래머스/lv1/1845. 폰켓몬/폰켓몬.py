def solution(nums):
    setnum = set(nums)
    if len(setnum) >= len(nums)//2 :
        answer = len(nums)//2
    else :
        answer = len(setnum)
    return answer