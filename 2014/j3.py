num_of_rounds = int(input())
rounds = tuple(tuple(map(int, input().split())) for _ in range(num_of_rounds))

antonia = 100
david = 100

for r in rounds:

    if r[0] > r[1]:
        david -= r[0]
    elif r[0] < r[1]:
        antonia -= r[1]

print(antonia)
print(david)
