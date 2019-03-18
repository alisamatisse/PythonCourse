
# coding: utf-8

# In[ ]:


a, b, c = [int(i) for i in (input('Введите три числа: ').split(' '))]
D = (b**2-4*a*c)**(1/2)
if isinstance(D, complex):
    print('Корней нет')
elif D > 0:
    x1 = (-b+D)/2*a
    x2 = (-b-D)/2*a
    print(f'Корней два:x1={x1}, x2={x2}')
elif D == 0:
    x = -b/2*a
    print(f'Корень один: х={x}')

