
# coding: utf-8

# In[36]:


numbers = [str(i) for i in input('Введите любое положительное число: ')]
print(numbers)
summ = 0
mult = 1
for i in range(len(numbers)):
    summ += int(numbers[i])
    mult *= int(numbers[i])
print(summ, mult)

