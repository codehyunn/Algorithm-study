from collections import Counter

def solution(X, Y):
    keys = list(set(X) & set(Y))
    x,y = Counter(X), Counter(Y)
    nums = [0 for _ in range(10)]
    for key in keys :
        cnt = x[key] if x[key] <= y[key] else y[key]
        nums[int(key)] = cnt
    
    answer = ''
    for idx, num in enumerate(nums):
        if num != 0 :
            answer = ''.join([str(idx)*num, answer])
    return "-1" if answer == '' else '0' if set(answer) == {'0'}  else answer