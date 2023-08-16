import sys

#sys.stdin = open('answer.txt', 'r')
input = sys.stdin.readline

n,k = map(int, input().split())
electronics = list(map(int, input().split()))

multi = []
answer = 0
for idx, elec in enumerate(electronics) :
    if elec in multi :
        continue
    
    if len(multi) < n :
        multi.append(elec)
        continue
    
    large_idx = -1
    large_elec = multi[0]
    for m in multi :
        m_idx = k+1 if m not in electronics[idx+1:] else electronics[idx+1:].index(m)
        if m_idx > large_idx :
            large_elec = m
            large_idx = m_idx
    
    answer += 1
    multi.remove(large_elec)
    multi.append(elec)
    
    
print(answer)