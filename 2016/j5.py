# 15/15

tp = int(input())
pop = int(input())

dmo = sorted(map(int, input().split()))
peg = sorted(map(int, input().split()))
pairs = []

for index in range(pop):

    if tp == 1:
        pairs.append([dmo[index], peg[index]])
    elif tp == 2:
        pairs.append([dmo[index], peg[(-1 * index) - 1]])

total = sum(map(max, pairs))

print(total)
