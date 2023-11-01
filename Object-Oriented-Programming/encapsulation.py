#OOP
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'Hello my name is {self.name} and i am {self.age} years old. ')
        
    def run(self, hello):
        print(f'my age is {self.age}, {hello}')
        
    @classmethod
    def adding_somthing(cls,number1, number2):
        return cls('Andrew', number1 + number2)

    @staticmethod
    def adding_things(number1,number2):
        return number1 + number2
    
player1 = PlayerCharacter('Andrew',22)
player1.speak()
print(player1.name)
print(player1.age)

player2 = {'name': 'Andrew', 'age': 22}
print(player2['name'])
print(player2['age'])