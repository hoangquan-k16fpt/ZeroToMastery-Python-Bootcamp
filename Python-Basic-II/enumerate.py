for i, char in enumerate([1,2,3,4]):
    print(i, char)
    
for i, char in enumerate(range(100)):
    print(i, char)
    if char == 50:
        print(f'index of 50 is {i}')