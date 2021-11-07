# 15/15

instructions = []
last_direction = None

while True:
    directions = input()

    if directions == "99999":
        break

    add = int(directions[0]) + int(directions[1])

    if add == 0:
        direction = last_direction
    elif add % 2 == 0:
        direction = "right"
    else:
        direction = "left"

    last_direction = direction

    instructions.append(f"{direction} {directions[-3:]}")

for instruction in instructions:
    print(instruction)
