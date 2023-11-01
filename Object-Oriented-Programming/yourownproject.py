#OOP
class PlayerCharacter:
    membership = True
    def __init__(self,name,age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age
    
    def shout(self):
        print(f'my name is {self.name}.')
        
    def run(self, hello):
        print(f'my age is {self.age}, {hello}')
        

player1 = PlayerCharacter(name='Cindy', age=20)
player2 = PlayerCharacter(name='Tom', age=34)

player1.run('hello')
player1.shout()
player2.attack = 500
print(player1.name, player1.age)
print(player2.name)
print(player2.attack)