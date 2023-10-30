picture = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    lst = []
    for pixel in row:
        if pixel:
            lst.append('*')
        else:
            lst.append(' ')
    print(''.join(lst))
    
for row in picture:
    for pixel in row:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')