some_list = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'n','n', 'm']

duplicates = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates)