"""
S = Sea Level
P = Atmospheric Pressure
B = Water Boiling Point

At S, P = 100 kPa, B = 100°C

+ S => -P, -B
- S => +P, +B

P = 5 x B - 400
"""

PRESSURE_AT_SL = 100


def find_pressure_from_boiling_point(boiling: int) -> int:
    """Finds the pressure from a provided boiling point"""

    pressure = 5 * boiling - 400

    return pressure


def determine_sea_level(pressure: int) -> int:
    """Determines the sea level with the provided pressure"""

    if pressure < PRESSURE_AT_SL:
        return 1
    elif pressure > PRESSURE_AT_SL:
        return -1

    return 0


boiling = int(input())
pressure = find_pressure_from_boiling_point((boiling))

print(pressure)
print(determine_sea_level((pressure)))
