def say_hello(name,emoji):
    print(f'helloooooo {name}, {emoji}')

say_hello('AndrewNgo',':)')
say_hello('Dan',':)')
say_hello('Andre',':)')
say_hello('Lisan',':)')

say_hello(':)', 'Daniel')
say_hello(emoji=':)', name='Daniel')

def say_hello_2(name='Philippe',emoji='^^'):
    print(f'helloooooo {name}, {emoji}')

say_hello_2()
say_hello_2(name='Uzel')