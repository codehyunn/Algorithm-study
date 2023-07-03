results = []
for i in range(1, 10001) :
    num = i
    result = num
    while num>=10 :
        result += num%10
        num //= 10
    result += num
    results.append(result)
    
for j in range(1,10001):
    if j not in results :
        print(j)