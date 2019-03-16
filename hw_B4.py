
# coding: utf-8

# In[ ]:


import random
rnumber = random.randint(1, 100)
def guessing_game():
    number = int(input('Введите число от 1 до 100, может быть Вы угадаете? '))
    if number == rnumber:
        print('Вы угадали, классно!')
    elif number > rnumber:
        print('Загаданное число меньше, пробуйте ещё!')
        guessing_game()
    elif number < rnumber:
        print('Загаданное число больше, пробуйте ещё!')
        guessing_game()
guessing_game()

