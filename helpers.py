import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Execution time for {func.__name__}: {end - start:.4f} seconds')
        return result
    return wrapper

@time_execution
def expensive_computation(n):
    total = 0
    for i in range(n):
        total += sum(j * j for j in range(1000))
    return total

@time_execution
def process_data(data):
    return [expensive_computation(item) for item in data]

if __name__ == '__main__':
    result = process_data(range(10))
    print(result)