basket = [1,2,3,4,5]
print(len(basket))

basket.append(100)
basket.extend([101,102,109])
basket.insert(2,9)
print(basket)

basket.pop()
basket.remove(100)
new_basket = basket.pop(6)
print(new_basket)
print(basket)
basket.clear()
print(basket)