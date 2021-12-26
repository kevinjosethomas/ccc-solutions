small_treats = input()
medium_treats = input()
large_treats = input()

happiness = small_treats + (2 * medium_treats) + (3 * large_treats)

if happiness >= 10:
    print("happy")
else:
    print("sad")
