#OOP
class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def shout(self):
        print(f'my name is {self.name}.')
        
    def run(self, hello):
        print(f'my age is {self.age}, {hello}')
        
    @classmethod
    def adding_somthing(cls,number1, number2):
        return cls('Andrew', number1 + number2)

    @staticmethod
    def adding_things(number1,number2):
        return number1 + number2
    
player3 = PlayerCharacter.adding_somthing(3,8)
print(player3.age)
print(PlayerCharacter.adding_things(4,39))
