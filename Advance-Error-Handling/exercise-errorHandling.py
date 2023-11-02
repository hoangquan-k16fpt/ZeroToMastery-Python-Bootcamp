tryTest = 0
success = False
while True:
    try:
        age = int(input('how old are you? '))
        print(age)
        age = 10/age
    except ValueError:
        print('Please enter a number')
        tryTest += 1
        continue
    except ZeroDivisionError:
        print('Please enter a number > 0')
        tryTest += 1
        continue
    else: 
        print('ok')
        success = True
        break
    finally:
        if not success:
            print(f'you have {5 - tryTest} try again')