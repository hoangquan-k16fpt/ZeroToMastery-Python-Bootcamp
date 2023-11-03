from random import randint
import sys

while True:
    try:
        ran_num = randint(int(sys.argv[1]), int(sys.argv[2]))
        my_num = int(input('Input your guess number: '))
        if my_num == ran_num:
            print('you are genius')
            break
        elif my_num < int(sys.argv[1]) or my_num > int(sys.argv[2]):
            print('Please enter a number in the range!')
    except ValueError:
        print('please enter a number')
        continue



