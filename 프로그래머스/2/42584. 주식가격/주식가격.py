from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices :
        now_price = prices.popleft()
        _answer = 0
        for comp_price in prices :
            _answer += 1
            if now_price > comp_price :
                break
            
        answer.append(_answer)
        
    return answer
