import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_non_empty_string(value: str) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_positive_integer(value) -> bool:
    return isinstance(value, int) and value > 0


def is_valid_url(url: str) -> bool:
    pattern = r'^(http|https)://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


def is_valid_phone_number(phone: str) -> bool:
    pattern = r'^[+]?\d{10,15}$'
    return bool(re.match(pattern, phone))
