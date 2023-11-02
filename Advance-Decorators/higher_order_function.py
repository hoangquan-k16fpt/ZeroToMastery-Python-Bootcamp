def hello(func):
    func()

def greet():
    def func():
        return 5
    return func

