import sys

input = sys.stdin.readline

while True :
    try :
        n = int(input())
        len_n = len(str(n))
        
        ones = '1' * len_n
        cnt = len_n

        while True:
            if int(ones) < n or int(ones) % n != 0 :
                ones += '1'
                cnt += 1
                continue
        
            print(cnt)
            break
        
    except :
        break