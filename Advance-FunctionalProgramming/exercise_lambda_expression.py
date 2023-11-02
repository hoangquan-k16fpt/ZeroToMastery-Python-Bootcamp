my_list = [5,4,3]
new_list = list(map(lambda item: item ** 2, my_list))
print(new_list)

your_list = [(0,2), (4,3), (10,-1), (9,9)]

your_list.sort(key= lambda x: x[1])
print(your_list)

their_list = [4,5,77,8,9,1,3,6,7,9,3,634,42,78,43,11,66,80,42,543,222,998,421,564]
their_list.sort()
print(their_list)
