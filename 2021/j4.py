# 9/15

from typing import Iterable

swaps = 0


def sort(shelf: Iterable):
    """Consecutively goes through a shelf and sorts it"""

    global swaps
    new_swaps = 0

    for index in range(len(shelf)):
        book = shelf[index]

        if index + 1 == len(shelf):
            break

        successor = shelf[index + 1]
        if book == successor or not book > successor:
            continue
        else:
            shelf[index] = successor
            shelf[index + 1] = book
            swaps += 1
            new_swaps += 1

    if new_swaps:
        shelf = sort(shelf)

    return shelf


shelf = sort([i for i in input()])

print("".join(shelf))
print(swaps)
