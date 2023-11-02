my_list = [1,2,3,4]
def multiplyby2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,my_list)))
print(list(map(multiplyby2, my_list)))
print(my_list)