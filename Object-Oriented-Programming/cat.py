# class Cat:
#     def __init__(self, cat1, cat2, cat3):
#         self.cat1 = cat1
#         self.cat2 = cat2
#         self.cat3 = cat3
        
#     def oldest_cat(self):
#         if self.cat1 > self.cat2 and self.cat1 > self.cat3:
#             print(f' cat1 is {self.cat1} years and the oldest')
#             return self.cat1
#         elif self.cat2 > self.cat3:
#             print(f'cat2 is {self.cat2} years and the oldest')
#             return self.cat2
#         else:
#             print(f'cat3 is {self.cat3} years and the oldest')
#             return self.cat3
    
# oldest_cat = Cat(1,2,3)
# oldest_cat.oldest_cat()

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
cat1 = Cat(name='Tommy', age=2)
cat2 = Cat(name='Bob', age=3)
cat3 = Cat(name='John', age=1)
cat4 = Cat(name='Nick', age=8)

cat_list = [cat1, cat2, cat3, cat4]
def oldest_Cat(lst):
    return max(lst)

oldest_cat = oldest_Cat([cat.age for cat in cat_list])

print(f'The oldest cat is {oldest_cat} years old.')