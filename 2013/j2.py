ALLOWED_CHARACTERS = ["I", "O", "S", "H", "Z", "X", "N"]

word = input().upper()

for char in word:

    if char not in ALLOWED_CHARACTERS:
        print("NO")
        exit()

print("YES")
