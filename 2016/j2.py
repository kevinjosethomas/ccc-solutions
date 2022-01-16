# 15/15

square = tuple(tuple(map(int, input().split())) for _ in range(4))

total = sum(square[0])

for index in range(4):
    if sum(square[index]) != total:
        print("not magic")
        exit()

    if sum(tuple(x[index] for x in square)) != total:
        print("not magic")
        exit()

print("magic")
