# 7/15

combinations = tuple(tuple(input().split()) for _ in range(3))

num_of_steps, original, final = input().split()


def substitute(string, steps, history):

    if steps == 0:
        if string == final:
            return history
        return False

    for index in range(len(string)):
        for number, combination in enumerate(combinations):
            start = max((index + 1) - len(combination[0]), 0)
            end = index + 1

            if string[start:end] == combination[0]:
                output = string[:start] + combination[1] + string[end:]

                if substitute(output, steps - 1, history) != False:
                    history.append((number + 1, start + 1, output))
                    return history

    return False


steps = substitute(original, int(num_of_steps), [])
steps.reverse()

for step in steps:
    print(" ".join(map(str, step)))
