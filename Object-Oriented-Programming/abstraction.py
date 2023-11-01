#OOP
class PlayerCharacter:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def speak(self):
        print(f'Hello my name is {self._name} and i am {self._age} years old. ')
        
    def run(self):
        print(f'my age is {self._age}')
        
    @classmethod
    def adding_somthing(cls,number1, number2):
        return cls('Andrew', number1 + number2)

    @staticmethod
    def adding_things(number1,number2):
        return number1 + number2
    
player1 = PlayerCharacter('Andrew',22)
player1.speak()
player1.run()