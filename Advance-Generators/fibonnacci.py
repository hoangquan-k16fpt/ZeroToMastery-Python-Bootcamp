from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'running on {end - start} ms')
        return result
    return wrapper

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
        
@performance
def run1():
    for i in fib(20):
        print(i)


def fib2(number):
    if number <= 1:
        return number
    else: 
        return fib2(number - 1) + fib2(number - 2)

@performance
def run2():
    for i in range(20):
        print(fib2(i))

run1()
run2()

def fib3(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib3(20))

        

