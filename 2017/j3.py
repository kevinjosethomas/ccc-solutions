# 15/15

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
battery = int(input())

x_diff = abs(start[0] - end[0])
y_diff = abs(start[1] - end[1])
min_steps = x_diff + y_diff

if battery < min_steps:
    print("N")
else:
    if min_steps % 2 == 0:
        if battery % 2 != 0:
            print("N")
        else:
            print("Y")
    else:
        if battery % 2 == 0:
            print("N")
        else:
            print("Y")
