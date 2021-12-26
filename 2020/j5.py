# 11/15

if __name__ == "__main__":
    f = open("../data.txt", "r")
    lines = f.readlines()

    width = int(lines[0])
    length = int(lines[1])
    room = tuple(tuple(map(int, lines[_ + 2].split())) for _ in range(width))
else:
    width = int(input())
    length = int(input())

    room = tuple(tuple(map(int, input().split())) for _ in range(width))


def find_path(product, history):

    if product == 1:
        return True

    for row in range(width):
        for col in range(length):
            if room[row][col] != product:
                continue

            if (row, col) in history:
                return False

            history.append((row, col))

            if find_path((row + 1) * (col + 1), history):
                return True

    return False


print("yes" if find_path(width * length, []) else "no")
