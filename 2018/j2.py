# 15/15

num_of_spots = int(input())
yesterday_spots = input()
today_spots = input()

total = 0

for index, spot in enumerate(yesterday_spots):
    if spot == "C" and today_spots[index] == "C":
        total += 1

print(total)
