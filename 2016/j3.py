# 15/15

string = input()

longest = 1

for length in range(2, len(string) + 1):

    for starting_point in range(len(string)):
        selected_string = string[starting_point : starting_point + length]

        if selected_string == selected_string[::-1]:
            longest = len(selected_string) if len(selected_string) > longest else longest

print(longest)
