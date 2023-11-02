def my_decorators(func):
    def wrap_func(*args,**kwargs):
        func(*args,**kwargs)
    return wrap_func

@my_decorators
def hello(emoji, greeting='hiiiii', cols= 10, rows= 50):
    print(greeting,emoji, cols, rows)
    
hello(':D')

