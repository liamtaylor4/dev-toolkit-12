def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))

def lerp(start, end, t):
    return start + (end - start) * t

import random

def random_choice(choices):
    return random.choice(choices)

def generate_random_int(min_value, max_value):
    return random.randint(min_value, max_value)

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def normalize(vector):
    length = calculate_distance((0, 0), vector)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

