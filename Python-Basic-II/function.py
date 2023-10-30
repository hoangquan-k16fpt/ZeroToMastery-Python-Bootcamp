def say_hello():
    print('helloooooooo')

say_hello()

picture = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

def show_diamond():
    for row in picture:
        lst = []
        for pixel in row:
            if pixel:
                lst.append('*')
            else:
                lst.append(' ')
        print(''.join(lst))
show_diamond()