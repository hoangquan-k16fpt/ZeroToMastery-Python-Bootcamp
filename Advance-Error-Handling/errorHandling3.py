tryTest = 0
success = False
while True:
    try:
        age = int(input('how old are you? '))
        print(age)
        raise ValueError('hey, cut it out')
    except ZeroDivisionError:
        print('Please enter a number > 0')
        tryTest += 1
        break
    else: 
        print('ok')
        success = True
        break
    finally:
        if not success:
            print(f'you have {5 - tryTest} try again')