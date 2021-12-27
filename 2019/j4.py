grid = [["1", "2"], ["3", "4"]]
instructions = input()

for instruction in instructions:
    if instruction == "H":
        grid.reverse()
    elif instruction == "V":
        grid[0].reverse()
        grid[1].reverse()

print(" ".join(grid[0]))
print(" ".join(grid[1]))
