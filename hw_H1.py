
# coding: utf-8

# In[ ]:


import time
import random

class Health:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def hp(current, damage):
        result_of_the_fight = current - damage
        return result_of_the_fight
    def add_hp(current, advantage = 5):
        new_hp = current + advantage
        return new_hp
        
        
class Zombie(Health):
    def __init__(self, name):
        self.name = name
        
    def attack(self, damage):
        return s.hp(current_hp_of_survivor, damage)


class Survivor(Health):
    def __init__(self, name):
        self.name = name
        
    def attack(self, damage):
        return z.hp(current_hp_of_zombie, damage)
    
class MathHelper(Health):
    def __init__(self, name):
        self.name = name
    def equation(self):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        result = x*y
        user_solution = int(input('You have a chance to help survivor. Solve this equation:{}*{} = '.format(x, y)))
        if result == user_solution:
            current_hp_of_survivor = s.add_hp(current_hp_of_survivor)
            print('Hooray, survivor gets 5 health points! God bless you.')
        
current_hp_of_zombie = 100
current_hp_of_survivor = 100
while True:
        s = Survivor('You')
        z = Zombie('Crazy dead walking')
        damage = random.randint(0, 20)
        current_hp_of_zombie = s.attack(damage)
        if current_hp_of_zombie < 0:
            print('Game is over for zombie')
            print("Survivor's health points are: {}".format(current_hp_of_survivor))
            break;
        print('{} damaged {} with {}'.format(s.name, z.name, damage))
        print("{}'s current health points are: {}".format(z.name, current_hp_of_zombie))
        damage = random.randint(0, 20)
        current_hp_of_survivor = z.attack(damage)
        if current_hp_of_survivor < 0:
            print('Game is over for you')
            print("Zombie's health points are: {}".format(current_hp_of_zombie))
            break;
        equation = MathHelper('helper')
        equation.equation()
        print('\n{} damaged {} with {}'.format(z.name, 'you', damage))
        print("{}r current health points are: {}\n".format(s.name, current_hp_of_survivor))
        time.sleep(2)

