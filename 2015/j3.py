ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
VOWEL_INDEXES = [ALPHABETS.index("a"), ALPHABETS.index("e"), ALPHABETS.index("i"), ALPHABETS.index("o"), ALPHABETS.index("u")]

string = input()
encrypted = ""

for char in string:

    if char in VOWELS:
        encrypted += char
        continue

    alpha_index = ALPHABETS.index(char)
    differences = []

    for vowel in VOWEL_INDEXES:
        differences.append(abs(vowel - alpha_index))

    closest_vowel = VOWELS[differences.index(min(differences))]

    next_index = alpha_index + 1
    if next_index in VOWEL_INDEXES:
        next_index += 1

    successing_char = ALPHABETS[min(25, next_index)]

    encrypted += char + closest_vowel + successing_char

print(encrypted)
