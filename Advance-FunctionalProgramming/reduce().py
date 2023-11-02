from functools import reduce
my_list = [1,2,3,4]
your_list = [10,20,30]
their_list = [50,100,300]
def multiplyby2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumalator(acc,item):
    print(acc,item)
    return acc + item

print(reduce(accumalator, my_list))

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

num = [2,4,5,7,9,32,43,6,76,55,32,91,88,432,65,44,97,75,43]
max = reduce(lambda x,y: x if x > y else y, num)
print(max)