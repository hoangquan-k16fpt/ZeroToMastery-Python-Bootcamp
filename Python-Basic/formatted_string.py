name = 'Andrew Ngo'
age = 22

print("Hello " + name + ". " + "You are " + str(age) + " years old")
print(f"Hello {name}. You are {age} years old.")
print("Hello {}. You are {} years old.".format(name, age))

print("Hello {new_name}. You are {age} years old.".format(new_name='Sally', age=100))