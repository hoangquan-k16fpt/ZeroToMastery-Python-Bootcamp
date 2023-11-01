def highest_even(lst):
    highest_even = 0
    for item in lst:
        if item % 2 == 0 and item > highest_even:
            highest_even = item
    return highest_even

print(highest_even([0,1,3,4,5,6,8,9,7,5,3,2,1,54,36,77,8,3,2,5,9,1]))

def highest_even_2(lst):
    even = []
    for item in lst:
        if item % 2 == 0:
            even.append(item)
    return max(even)

print(highest_even_2([0,1,3,4,5,6,8,9,7,5,3,2,1,54,36,77,8,3,2,5,9,1]))