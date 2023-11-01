class User:      
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('do nothing')
        
class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attack with power {self.power}')
        super().attack()
        
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'attack with left - {self.num_arrows}')
        super().attack()
        
    def run(self):
        print('run faster')
        
class Hybrid(Wizard,Archer):
    def __init__(self,name,power,num_arrows):
        Wizard.__init__(self,name,power)
        Archer.__init__(self,name,num_arrows)

hb1 = Hybrid(name='Boige', power=50, num_arrows=100)

hb1.sign_in()
hb1.attack()
hb1.run()
print(hb1.name)