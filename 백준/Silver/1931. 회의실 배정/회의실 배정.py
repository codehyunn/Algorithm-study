n = int(input(""))
ans, endtime = 0, 0
schedule = []
for i in range(n) :
    times = list(map(int, input("").split()))
    schedule.append(times)

schedule.sort(key=lambda x : (x[1],x[0]))

for sche in schedule :
    if sche[0] >= endtime :
        endtime = sche[1]
        ans += 1

print(ans)