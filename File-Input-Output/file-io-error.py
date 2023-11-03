# try:
#     with open('sad.txt', mode='x') as myfile:
#         print(myfile.readline())
# except FileNotFoundError as err:
#     print(f'file not found {err}')
# except IOError as err:
#     print(f'IO error : {err}')

try:
    with open('sadty.txt', mode='r') as myfile:
        print(myfile.readline())
except FileNotFoundError as err:
    print(f'file not found {err}')
except IOError as err:
    print(f'IO error : {err}')