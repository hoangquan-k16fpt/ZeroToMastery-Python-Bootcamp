my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

your_list = [char for char in 'hello']
print(your_list)

my_list_2 = [num for num in range(0,100) if num % 2 == 0]
my_list_3 = [num*2 for num in range(0,100)]
print(my_list_2)
print(my_list_3)