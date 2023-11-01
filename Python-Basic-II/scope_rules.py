a = 1
def confusion():
    a = 5
    return a 

print(a)
print(confusion())

def parents():
    a=100
    def confusion2():
        return a
    return confusion2()


print(parents())