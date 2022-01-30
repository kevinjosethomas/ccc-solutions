year = int(input())

next_year = year + 1
while True:

    string = str(next_year)

    if len(set(string)) == len(string):
        print(next_year)
        exit()

    next_year += 1
