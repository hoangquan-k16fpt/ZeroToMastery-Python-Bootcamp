import re

pattern = re.compile('this')
string = 'search this inside of this text please!Andrei'

# print('search' in string)

# this_ = re.search('this', string)
# print(this_.start())
# print(this_.span())

this_ = pattern.search(string)
print(this_.group())
this__ = pattern.findall(string)
print(this__)

pattern2 = re.compile('search this inside of this text please!')
a = pattern2.fullmatch(string)
print(a)
b = pattern2.match(string)
print(b)
