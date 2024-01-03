import sys

input = sys.stdin.readline

while True :
    try :
        n = int(input())
        
        ones = 1
        cnt = 1

        while True:
            if ones % n != 0 :
                ones = ones*10+1
                cnt += 1
                continue
        
            print(cnt)
            break
        
    except :
        break