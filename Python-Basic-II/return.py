def sum(num1, num2):
    print('hihiii')
    return num1 + num2

print(sum(10,5))

total = sum(10,5)
print(sum(total,5))

def sum(num1, num2):
    def another_Sum(num1, num2):
        return num1 + num2
    return another_Sum(num1, num2)

total = sum(10,20)
print(total)