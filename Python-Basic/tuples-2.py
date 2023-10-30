my_tuples = (1,2,3,4,5,5)
new_tuple = my_tuples[1:4]
print(new_tuple)

x,y,z,*other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(other)
print(my_tuples.count(1))
print(my_tuples.index(5))
print(len(my_tuples))