dictionary = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}

print(dictionary)

dictionary_2 = {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True,
}

print(dictionary_2)
print(dictionary_2['a'][1])

mylist = [
    {
        'a' : [1,2,3],
        'b' : 'hello',
        'c' : True,
    },
    {
        'a' : [4,5,6],
        'b' : 'world',
        'c' : False,
    }
]

print(mylist[0]['b'])