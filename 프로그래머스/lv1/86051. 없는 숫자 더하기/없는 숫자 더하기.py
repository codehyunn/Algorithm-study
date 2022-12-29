def solution(numbers):
    all_nums = [i for i in range(10)]
    answer = sum([n for n in all_nums if n not in numbers])
    return answer