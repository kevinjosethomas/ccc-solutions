"""
S = Sea Level
P = Atmospheric Pressure
B = Water Boiling Point

At S, P = 100 kPa, B = 100°C

+ S => -P, -B
- S => +P, +B

P = 5 x B - 400
"""

from sys import stdin

PRESSURE_AT_SL = 100


def find_pressure_from_boiling_point(boiling: int) -> int:
    """Finds the pressure from a provided boiling point"""

    pressure = 5 * boiling - 400

    return pressure


def determine_sea_level(pressure: int) -> int:

    if pressure < PRESSURE_AT_SL:
        return 1
    elif pressure > PRESSURE_AT_SL:
        return -1
    else:
        return 0


B = int(stdin.readline())
P = find_pressure_from_boiling_point((B))

print(P)
print(determine_sea_level((P)))
