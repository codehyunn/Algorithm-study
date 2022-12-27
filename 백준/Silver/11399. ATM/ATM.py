n = int(input(''))

times = list(map(int, input('').split()))
times.sort()

anslist = [times[i]*(n-i) for i in range(n)]
ans = sum(anslist)

print(ans)