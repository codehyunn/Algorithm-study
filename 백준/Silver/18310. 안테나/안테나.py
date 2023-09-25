import sys
input = sys.stdin.readline

n = int(input())
houses = sorted(list(map(int, input().split())))

if n % 2 == 1 :
    print(houses[n//2])

else :
    a,b = 0,0
    for house in houses :
        a += abs(house-houses[n//2-1])
        b += abs(house-houses[n//2])

    if a <= b :
        print(houses[n//2-1])
        
    else :
        print(houses[n//2])