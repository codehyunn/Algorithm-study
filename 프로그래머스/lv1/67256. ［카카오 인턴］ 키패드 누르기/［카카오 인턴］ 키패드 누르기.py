def solution(numbers, hand):
    answer = ''
    hands_pos = [9, 11]
    
    for n in numbers :
        pos = n-1
        if pos < 0 : pos = 10
        if pos%3 == 1 :
            left,right = [(abs((x%3)-(pos%3))+abs((x//3)-(pos//3))) for x in hands_pos]
            if left == right :
                used_hand = hand[0].upper()
            else :
                used_hand = "L" if left == min(left,right) else "R"
        else :
            used_hand = "L" if pos%3 == 0 else "R"
             
        answer += used_hand
        idx = 0 if used_hand == 'L' else 1
        hands_pos[idx] = pos
        
    return answer
