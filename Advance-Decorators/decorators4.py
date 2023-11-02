from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'running on {end - start} ms')
        return result
    return wrapper

@performance
def running():
    for item in range(100000000):
        item * 5

running()