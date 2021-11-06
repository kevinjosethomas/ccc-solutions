from sys import stdin

bids = []
number_of_bids = int(stdin.readline().rstrip())

for i in range(number_of_bids * 2):
    value = stdin.readline().rstrip()

    if i % 2 == 0:
        bids.append([i, value])
    else:
        value = int(value)
        bids[len(bids) - 1].append(value)


bids.sort(key=lambda x: x[2], reverse=True)

winners = sorted([bid for bid in bids if bid[2] == bids[0][2]], key=lambda x: x[0])

print(winners[0][1])
