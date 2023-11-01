class User:
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('do nothing')
        
class Wizard(User):
    def __init__(self,name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attack with power {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'attack with left - {self.num_arrows}')
        
wizard1 = Wizard(name='Athur', power=50, email='hoangquan12@gmail.com')
archer1 = Archer(name='Robin', num_arrows= 400)
wizard1.sign_in()
archer1.sign_in()
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(archer1,User))

def player_attack(role):
    role.attack()

player_attack(wizard1)
print(wizard1.email)