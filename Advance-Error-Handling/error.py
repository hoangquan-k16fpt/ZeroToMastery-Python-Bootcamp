while True:
    try:
        age = int(input('how old are you? '))
        age = 10/age
        print(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a number > 0')
    else: 
        break
        