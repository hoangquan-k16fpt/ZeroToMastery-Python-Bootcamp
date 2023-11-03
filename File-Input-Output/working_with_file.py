
# my_files = open('text.txt')
# print(my_files.read())
# my_files.seek(0)
# print(my_files.read())
# my_files.seek(0)
# print(my_files.read())

my_files2 = open('text.txt')
# print(my_files2.readline())
# print(my_files2.readline())
# print(my_files2.readline())
print(my_files2.readlines())
my_files2.close()