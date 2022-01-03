# 15/15

number = "".join([input() for i in range(4)])


def determine_number(num):

    if (num[0] != "8" and num[0] != "9") or (num[-1] != "8" and num[-1] != "9") or (num[1] != num[2]):
        return False

    return True


print("ignore" if determine_number(number) else "answer")
