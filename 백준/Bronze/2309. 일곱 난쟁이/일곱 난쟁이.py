import sys
from itertools import combinations

input = sys.stdin.readline

heights = []
for i in range(9) :
    heights.append(int(input()))
    
total = sum(heights)
over = total - 100

for x,y in list(combinations(heights,2)) :
    if x+y == over :
        heights.remove(x)
        heights.remove(y)
        break

heights.sort()

for h in heights:
    print(h)