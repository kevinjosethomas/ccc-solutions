long_string = input()
short_string = input()

manipulated_string = short_string

for _ in range(len(short_string)):
    if manipulated_string in long_string:
        print("yes")
        exit()

    manipulated_string = manipulated_string[1:] + manipulated_string[0]

print("no")
