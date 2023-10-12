import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))

count = 0 
cards = [i%3 for i in range(N)]
while True :
    if P == cards :
        print(count)
        exit()
    
    if count and cards == [i%3 for i in range(N)] :
        print(-1)
        exit()
        
    new_cards = [-1 for _ in range(N)]
    for next_idx, curr_idx in enumerate(S) :
        new_cards[next_idx] = cards[curr_idx]
    cards = new_cards
    
    count += 1