number_of_lines = int(input())

output = []

for _ in range(number_of_lines):
    line = input().split()

    output.append(line[1] * int(line[0]))

for decoded in output:
    print(decoded)
