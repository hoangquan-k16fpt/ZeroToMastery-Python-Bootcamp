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
@performance
def running2():
    for item in list(range(100000000)):
        item * 5

running()
running2()