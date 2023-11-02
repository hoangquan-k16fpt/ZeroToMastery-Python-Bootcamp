def my_decorators(func):
    def wrap_func():
        print('nice to meet you')
        func()
        print('how are you')
    return wrap_func

@my_decorators
def hello():
    print('helooooooooo')
hello()


hello2 = my_decorators(hello)
hello2()