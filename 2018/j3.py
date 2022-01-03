# 15/15

distances = list(map(int, input().split()))
cities = [0, sum(distances[:1]), sum(distances[:2]), sum(distances[:3]), sum(distances[:4])]

output = []

for city in cities:
    intervals = []
    for city2 in cities:
        intervals.append(str(abs(city - city2)))

    output.append(" ".join(intervals))

for line in output:
    print(line)
