import sys

input = sys.stdin.readline

H,W = map(int, input().split())
blocks = list(map(int, input().split()))

prev_block = blocks[0]
count = [0]

for idx, block in enumerate(blocks) :
    if idx == 0 :
        continue
    
    if idx == len(blocks)-1 :
        if prev_block > block :
            for i in range(len(count)-1, -1, -1) :
                block = max(block, blocks[i])
                count[i] = max(0, count[i]-(prev_block - block))
        continue
                
    if prev_block > block :
        count.append(prev_block-block)
    else :
        prev_block = block
        count.append(0)

print(sum(count))