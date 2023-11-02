my_list = [1,2,3,4]
your_list = [10,20,30]
their_list = [50,100,300]

def only_odd(item):
    return item % 2 != 0

def accumalator(acc,item):
    print(acc,item)
    return acc + item

multiply_by2 = list(map(lambda item: item*2, my_list))
print(multiply_by2)

check_odd = list(filter(lambda item: item % 2 != 0, their_list))

check_leaf_year_ = lambda year: True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
print(check_leaf_year_(2002))

