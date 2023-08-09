import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5 :
    print(0)
    exit(0)
    
if k == 26 :
    print(n)
    exit(0)
    
k -= 5
    
base = ['a', 'c', 'i', 'n', 't']
words,total = [], []

for i in range(n) :
    bit_word = 0
    word = list(set((input().strip())[4:-4]) - set(base))
  
    for w in word :
        bit_word |= (1 << (ord(w)-ord('a')))
        
    words.append(bit_word)
    
    total.extend(word)
    total = list(set(total))

if len(total) < k :
    print(n)
    exit(0)
    
combination = list(combinations(total, k))

max_count = 0
for com in combination :
    bit_com = 0
    for c in com :
        bit_com |= (1<<(ord(c)-ord('a')))
    
    count = 0
    for idx, word in enumerate(words) :
        if (word & (~bit_com)) == 0 :
            count += 1
    
    max_count = max(max_count, count)

print(max_count)