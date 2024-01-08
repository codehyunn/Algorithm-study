import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_to_num = dict()
num_to_pocketmon = dict()

for i in range(1, N+1) :
    mon = input().rstrip()
    pocketmon_to_num[mon] = i
    num_to_pocketmon[i] = mon

for _ in range(M) :
    m = input().rstrip()
    if m.isdigit() :
        m = int(m)
        print(num_to_pocketmon[m])
    else : 
        print(pocketmon_to_num[m])