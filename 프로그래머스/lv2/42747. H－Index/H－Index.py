def solution(citations):
    for i in range(max(citations), -1, -1) :
        paper = sum([1 for x in citations if x>=i])
        if paper >= i:
            return i