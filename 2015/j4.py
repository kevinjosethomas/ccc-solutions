# 10/15

num_of_messages = int(input())
messages = []
wait_times = {}

for i in range(num_of_messages):

    msg = input().split()
    meta = (msg[0], int(msg[1]))

    try:
        if not messages[-1][0] == "W" and msg[0] != "W":
            messages.append(("W", 1))
    except:
        pass

    messages.append(meta)

recipients = list(set([msg[1] for msg in messages if msg[0] != "W"]))
recipients.sort()

for recipient in recipients:

    filtered_messages = [msg for msg in messages if msg[0] == "W" or (msg[0] != "W" and msg[1] == recipient)]

    while filtered_messages[0][0] == "W":
        filtered_messages.pop(0)

    while filtered_messages[-1][0] == "W":
        filtered_messages.pop()

    waiting = False
    for ind, msg in enumerate(filtered_messages[:]):
        if msg[0] == "R":
            waiting = True
            continue

        if msg[0] == "S":
            waiting = False
            continue

        if not waiting and msg[0] == "W":
            filtered_messages.pop(ind)

    if filtered_messages[-1][0] == "R":
        wait_times[recipient] = -1
        continue

    time = sum([msg[1] for msg in filtered_messages if msg[0] == "W"])
    wait_times[recipient] = time

for recipient in wait_times:
    print(f"{recipient} {wait_times[recipient]}")

    #  3
