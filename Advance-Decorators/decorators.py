def hello():
    print('heloooooooooo')
    
greet = hello
del hello

print(greet())

def hi(func):
    func()
    
def greet():
    print('hiiiiii')

a = hi(greet)
print(a)