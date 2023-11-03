from collections import Counter, OrderedDict, defaultdict

li = [1,2,3,4,5,6,7,8,9,9,3,4,5,5,5,3,2,2,1]
print(Counter(li))
sentences = 'bla bla balh blahh hello python hello world'
print(Counter(sentences))
dictionary = defaultdict( lambda: 'bla bla balh blahh',{'a':1, 'b':2, 'c':3})
print(dictionary['d'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

d2 = OrderedDict()
d2['a'] = 1
d2['c'] = 3
d2['b'] = 2

print(d2 == d)