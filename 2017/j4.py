# 15/15

time_watched = int(input())


def find_number_of_arithmetic_sequences(minutes):

    num_of_sequences = 0

    while minutes > 0:
        for hour in range(0, 12):
            for minute in range(0, 60):

                if minutes == 0:
                    return num_of_sequences
                minutes -= 1

                if hour == 0:
                    hour = 12

                intervals = []

                digits = tuple(str(hour) + ("0" + str(minute) if minute < 10 else str(minute)))

                for index, digit in enumerate(digits):

                    if index + 1 == len(digits):
                        break

                    successor = int(digits[index + 1])
                    intervals.append(successor - int(digit))

                if intervals.count(intervals[0]) == len(intervals):
                    num_of_sequences += 1

    return num_of_sequences


if time_watched > 720:
    total_sequences = ((time_watched // 720) * 31) + find_number_of_arithmetic_sequences((time_watched % 720) + 1)
else:
    total_sequences = find_number_of_arithmetic_sequences(time_watched + 1)

print(total_sequences)
