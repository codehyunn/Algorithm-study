def solution(absolutes, signs):
    signs = list(map(lambda x : -1 if x==False else 1, signs))
    answer = sum([absolutes[i]*signs[i] for i in range(len(absolutes))])
    return answer