import re

pattern = re.compile(r'([a-zA-Z0-9-.+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

password_pattern = re.compile(r'([a-zA-Z0-9$%#@&*!?]{8,}\d)')

while True: 
    try:
        a = pattern.search(string= input('input your email address: '))
        if a:
            while True:
                try:
                    password_ = password_pattern.fullmatch(string=input('input your password: '))
                    if password_:
                        print('your account was created successfully.')
                        break
                    else:
                        raise Exception('please enter a valid password')
                except Exception as err:
                    print(f'{err}')
                    continue
            break
        else:
            raise Exception('please enter a valid email address!')
    except Exception as err:
        print(f'{err}')
        continue    

