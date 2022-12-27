m = int(input(''))
m = 1000 - m
ans = 0 

while True :
    if m >= 500 :
        ans += (m//500)
        m %= 500
    elif m >= 100 :
        ans += (m//100)
        m %= 100
    elif m >= 50 :
        ans += (m//50)
        m %= 50
    elif m >= 10 :
        ans += (m//10)
        m %= 10
    elif m >= 5 :
        ans += (m//5)
        m %= 5
    else :
        ans += m
        break

print(ans)