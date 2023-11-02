your_list = {char for char in 'hello'}
print(your_list)

my_list_2 = {num for num in range(0,100) if num % 2 == 0}
my_list_3 = {num*2 for num in range(0,100)}
print(my_list_2)
print(my_list_3)

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
}

my_dict = {k:v**2 for k,v in simple_dict.items()}
print(my_dict)

my_dict_2 = {num : num + 2 for num in [2,3,4,5,6]}
print(my_dict_2)