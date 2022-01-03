# 15/15

a_three = int(input())
a_two = int(input())
a_one = int(input())

b_three = int(input())
b_two = int(input())
b_one = int(input())

apples = (a_three * 3) + (a_two * 2) + a_one
bananas = (b_three * 3) + (b_two * 2) + b_one

if apples > bananas:
    print("A")
elif apples < bananas:
    print("B")
else:
    print("T")
