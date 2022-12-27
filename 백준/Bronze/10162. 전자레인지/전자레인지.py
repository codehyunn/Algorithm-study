a, b, c = 300, 60, 10
T = int(input(''))
ans = [0 for _ in range(3)]

while True :
    if T % c != 0 :
        ans = -1
        break

    if T >= a :
        ans[0] += (T//a)
        T %= a

    elif T >= b :
        ans[1] += (T//b)
        T %= b
    
    elif T >= c :
        ans[2] += (T//c)
        T %= c

    else :
        break

if ans == -1 :
    print(ans)
else :
    for a in ans :
        print(a, end=' ')