n = int(input(''))
weights = []
for i in range(n) :
    weights.append(int(input('')))
weights.sort()

k = [(n-i)*weights[i] for i in range(n)]
ans = max(k)

print(ans)