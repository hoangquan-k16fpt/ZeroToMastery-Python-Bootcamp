my_list = [1,2,3,4]
your_list = [10,20,30]
their_list = [50,100,300
              ]
def multiplyby2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list,your_list,their_list)))
