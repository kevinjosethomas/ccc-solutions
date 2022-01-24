num_of_students = int(input())
order1 = input().split()
order2 = input().split()

pairs = {}

for index in range(num_of_students):

    first = order1[index]
    last = order2[index]

    if first == last:
        print("bad")
        exit()

    if first in pairs.keys():
        if last != pairs[first]:
            print("bad")
            exit()

    if last in pairs.keys():
        if first != pairs[last]:
            print("bad")
            exit()

    pairs[first] = last
    pairs[last] = first

print("good")
