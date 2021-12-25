rows = int(input())  # M
columns = int(input())  # N
num_of_instructions = int(input())  # K

instructions = {}

for _ in range(num_of_instructions):

    instruction = input()
    stored = instructions.get(instruction)

    if stored:
        instructions[instruction] += 1
    else:
        instructions[instruction] = 1

total_golds = 0

for col in range(columns):
    for row in range(rows):
        total = instructions.get(f"R {row+1}", 0) + instructions.get(f"C {col+1}", 0)

        if total % 2 != 0:
            total_golds += 1


print(total_golds)
