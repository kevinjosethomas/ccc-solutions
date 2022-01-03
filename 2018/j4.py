# 15/15

num_of_flowers = int(input())

table = [list(map(int, input().split())) for _ in range(num_of_flowers)]


def rotate_table(tb):

    new_table = [[] for i in range(num_of_flowers)]

    for row in reversed(tb):
        for index, flower in enumerate(row):
            new_table[index].append(flower)

    originals = []

    for row in new_table:
        last_flower = 0
        originals.append(row[0])

        for flower in row:
            if flower > last_flower:
                last_flower = flower
            else:
                return rotate_table(new_table)

    last_original = 0
    for original in originals:
        if original > last_original:
            last_original = original
        else:
            return rotate_table(new_table)

    return new_table


initial_table = rotate_table(table)

for row in initial_table:
    print(" ".join(map(str, row)))
