def super_func(name, *args, hi = 'hello', **kwargs):
    total = 0
    print(kwargs)
    print(args)
    print(*args)
    for item in kwargs.values():
        total += item
    return sum(args) + total

result = super_func('Andrew', 1,2,3,4,5,6,7, number1 = 10, number2=20)
print(result)