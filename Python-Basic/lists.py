list1 = [1,2,3,4,5,6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
list3 = [1,2, 'a', 'b', True, 'hello']
amazon_cart = [
    'notebook', 
    'sunglasses',
    'toys',
    'grapes',]
print(amazon_cart[0:])
print(amazon_cart[0::2])
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
print(amazon_cart[0::2])
print(new_cart)
new_cart[1] = 'singum'
print(new_cart)