number_of_lines = int(input())

compressed_messages = []

for _ in range(number_of_lines):
    decompressed = input()

    compressed = ""
    symbol = ""
    count = 0

    for character in decompressed:
        if not symbol:
            symbol = character
            count = 1
            continue

        if character == symbol:
            count += 1
            continue

        compressed += f"{count}{symbol}"

        symbol = character
        count = 1

    compressed += f"{count}{symbol}"

    compressed_messages.append(compressed)

for message in compressed_messages:
    print(message)
