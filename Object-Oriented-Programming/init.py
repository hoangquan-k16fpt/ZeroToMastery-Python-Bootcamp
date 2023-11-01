#OOP
class PlayerCharacter:
    membership = True
    def __init__(self,name='anonymous',age = 0):
        if (age > 18):
            self.name = name
            self.age = age
    
    def shout(self):
        print(f'my name is {self.name}.')
        
    def run(self, hello):
        print(f'my age is {self.age}, {hello}')
        

player1 = PlayerCharacter(name='Cindy', age=10)
print(player1.name)
# player1.run('hello')
# player1.shout()
# print(player1)