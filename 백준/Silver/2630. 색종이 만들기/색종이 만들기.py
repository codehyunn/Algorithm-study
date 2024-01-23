import sys

input = sys.stdin.readline

n = int(input()) # 2,4,8,16,32,64,128
paper = [list(map(int,input().split())) for _ in range(n)]

blue, white = 0,0

def check(n, paper) :
    global blue, white
    if n == 1 :
        return
    
    half_n = n//2
    split_paper, color = [[] for _ in range(4)], []
    
    for i in range(half_n) :
        lines = [paper[i][:half_n], paper[i][half_n:],paper[i+half_n][:half_n],paper[i+half_n][half_n:]]

        for j in range(4) :
            split_paper[j].append(lines[j])
            _sum = sum(lines[j])
            
            if i == 0 :
                if _sum == 0 or _sum == half_n :
                    color.append(_sum)
                else :
                    color.append(-1)
                
            else :
                if _sum == color[j] :
                    continue
                else :
                    color[j] = -1

    if color.count(half_n) == 4 :
        blue += 1
    elif color.count(0) == 4 :
        white += 1
    else :
        for i in range(4) :
            if color[i] == -1 :
                check(n//2, split_paper[i])
            elif color[i] == half_n :
                blue += 1
            else :
                white += 1

check(n, paper)

print(white)
print(blue)