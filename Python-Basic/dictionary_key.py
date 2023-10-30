dictionary = {
    '123' : [1,2,3],
    True : 'hello',
    '[100]' : True,
}

print(dictionary)
print(dictionary['123'][1])
print(dictionary[True])

dictionary_2 = {
    '123' : [1,2,3],
    '123' : 'hello',
    '[100]' : True,
}

print(dictionary_2['123'][2])