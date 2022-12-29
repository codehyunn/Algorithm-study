def solution(price, money, count):
    count_sum = (count*(count+1))/2
    answer = price*count_sum - money
    if answer < 0 :
        answer = 0
    return answer