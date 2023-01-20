def solution(food):
    answer = '0'
    food[1:] = [i-1 if i%2==1 else i for i in food[1:]]
    for i in range(len(food)-1,0,-1) :
        answer = str(i)*(food[i]//2) + answer + str(i)*(food[i]//2)
    return answer