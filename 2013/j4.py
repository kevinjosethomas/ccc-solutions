duration = int(input())
num_of_chores = int(input())
chores = sorted([int(input()) for _ in range(num_of_chores)])

possible_chores = 0
for chore in chores:
    if duration - chore >= 0:
        possible_chores += 1
        duration -= chore
    else:
        break

print(possible_chores)
