n,k = map(int, input('').split())
values = []
for i in range(n) :
    values.append(int(input('')))
values.sort(reverse=True)
ans = 0

for i in range(n) :
    if k >= values[i] :
        ans = ans + (k//values[i])
        k %= values[i]

print(ans)