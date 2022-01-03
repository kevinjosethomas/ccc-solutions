# 15/15

small_treats = int(input())
medium_treats = int(input())
large_treats = int(input())

happiness = small_treats + (2 * medium_treats) + (3 * large_treats)

if happiness >= 10:
    print("happy")
else:
    print("sad")
