def solution(n):
    nums = []
    while n > 2 :
        nums.append(n%3)
        n //= 3
    nums.append(n)
    answer = sum([(3**i)*nums[len(nums)-1-i] for i in range(len(nums))])
    return answer