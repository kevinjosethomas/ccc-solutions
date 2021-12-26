num_of_flicks = int(input())

art = []

for _ in range(num_of_flicks):
    coords = input().split(",")

    art.append((int(coords[0]), int(coords[1])))

lowest_x = min(art, key=lambda x: x[0])[0] - 1
lowest_y = min(art, key=lambda x: x[1])[1] - 1
highest_x = max(art, key=lambda x: x[0])[0] + 1
highest_y = max(art, key=lambda x: x[1])[1] + 1

print(f"{lowest_x},{lowest_y}")
print(f"{highest_x},{highest_y}")
