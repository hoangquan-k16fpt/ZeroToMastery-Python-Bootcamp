user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20,
}

print('basket' in user)
print('size' in user)
print('hello' in user.keys())
print('hello' in user.values())
print('greet' in user.keys())
print(user.items())

user2 = user.copy()
print(user2)
print(user)

print(user.pop('age'))
print(user.popitem())
print(user.update({'age': 99}))
print(user)