import random
import math

def roll_dice(sides=6, times=1):
    return [random.randint(1, sides) for _ in range(times)]


def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def random_item(items):
    return random.choice(items)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def is_power_of_two(n):
    return n and (n & (n - 1)) == 0


def lerp(start, end, t):
    return start + (end - start) * t