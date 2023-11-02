def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result

my_list = make_list(100)
print(my_list)

def generator_function(num):
    for item in range(num):
        yield item

g = generator_function(1000)
next(g)
