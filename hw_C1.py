
# coding: utf-8

# In[25]:


ls = [int(i) for i in input('Введите любое количество любых чисел: ').split(' ')]
for i in range(len(ls)):
        if i == len(ls)-1:
            break;
        if (ls[i+1] > ls[i]):
            print(ls[i+1])

