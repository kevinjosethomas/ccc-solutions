# 15/15


def output(mins):

    hour = mins // 60
    minute = mins % 60

    if hour >= 24:
        hour = hour % 24

    string = ""

    if hour < 10:
        string += f"0{str(hour)}:"
    else:
        string += f"{str(hour)}:"

    if minute < 10:
        string += f"0{str(minute)}"
    else:
        string += str(minute)

    return string


departure = tuple(map(int, input().split(":")))
distance_travelled = 0
time_travelled = 0

rush_hour = ((7, 10), (15, 19))

for minutes in range(300):

    if distance_travelled >= 120:
        break

    new_time = []

    if departure[1] + minutes >= 60:
        h = departure[0] + (minutes // 60)
        m = departure[1] + (minutes % 60)

        if m >= 60:
            h += m // 60
            m = m % 60

        if h >= 24:
            h = h % 24

        new_time.append(h)
        new_time.append(m)
    else:
        new_time.append(departure[0])
        new_time.append(departure[1] + minutes)

    if rush_hour[0][0] <= new_time[0] < rush_hour[0][1] or rush_hour[1][0] <= new_time[0] < rush_hour[1][1]:
        distance_travelled += 0.5
    else:
        distance_travelled += 1

    time_travelled += 1

print(output((departure[0] * 60) + departure[1] + time_travelled))
