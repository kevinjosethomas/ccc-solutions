# 15/15

n = int(input())
k = int(input())
total = n

for i in range(k):
    total += n * (10 ** (i + 1))

print(total)
