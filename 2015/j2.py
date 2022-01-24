string = input()

if ":-)" not in string and ":-(" not in string:
    print("none")
    exit()

happy = string.count(":-)")
sad = string.count(":-(")

if happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")
