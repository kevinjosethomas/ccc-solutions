one = int(input())
two = int(input())
three = int(input())

if one + two + three != 180:
    print("Error")
elif one == two == three == 60:
    print("Equilateral")
elif one != two and one != three and two != three:
    print("Scalene")
else:
    print("Isosceles")
