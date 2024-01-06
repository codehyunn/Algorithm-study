import sys

input = sys.stdin.readline

N = int(input()) # 이동하려는 채널
only_direct = abs(N-100)

M = int(input()) # 고장난 버튼 수
if M == 0 :
    print(min(len(str(N)), only_direct))
    exit()
    
broken = [False] * 10
temp = list(map(int, input().split()))
for t in temp :
    broken[t] = True

def movable(x) :
    for i in str(x) :
        if broken[int(i)] :
            return False
    return True 

def count(x) :
    return len(str(x)) + abs(N-x)

if N == 100  :
    print(0)
    exit()

answer = only_direct
for i in range(N, -1, -1) :
    if movable(i) : 
        answer = min(answer, count(i))
        break

i = N+1
while count(i) <= only_direct :
    if movable(i) :
        answer = min(answer, count(i))
        break
    i += 1 

print(answer)