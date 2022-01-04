# 3/15

num_of_pages = int(input())  # < 10000

visited = set()
shortest_path = 0
instructions = [list(map(int, input().split()))[1:] for _ in range(num_of_pages)]


def choose_paths(page, history):

    if page not in visited:
        visited.add(page)

    if not len(instructions[page - 1]):  # if this page doesn't need to lead ot any more (it is an ending)
        global shortest_path
        if shortest_path == 0 or len(history) + 1 < shortest_path:
            shortest_path = len(history) + 1
        return

    history.append(page)

    for p in filter(lambda x: x not in history, instructions[page - 1]):
        choose_paths(p, history)

    history.pop()

    return


choose_paths(1, [])
print("Y" if len(visited) == len(instructions) else "N")
print(shortest_path)
