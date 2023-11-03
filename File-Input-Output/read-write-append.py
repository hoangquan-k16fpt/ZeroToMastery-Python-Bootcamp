with open('text.txt', mode='a') as my_file:
    text = my_file.write('hey, it\'s me\n')
    print(text)
    
# with open('sad.txt', mode='w') as my_file:
#     text = my_file.write(':(')
#     print(text)

with open('sad.txt', mode='r+') as my_file:
    text = my_file.write(':)')
    print(text)
