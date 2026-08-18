import time
import requests
from functools import wraps

def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.ConnectionError as e:
                    attempts += 1
                    time.sleep(delay)
                    if attempts == max_retries:
                        raise e
        return wrapper
    return decorator

@retry(max_retries=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()