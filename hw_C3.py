
# coding: utf-8

# In[2]:


words = [str(i) for i in input('Введите какое-нибудь предложение: ').split(' ')]
longest = ''
for i in range(len(words)):
        if i+1 < len(words):
            if len(words[i+1]) > len(words[i]):
                longest = words[i+1]
print(f'Самое длинное слово, которые Вы ввели: {longest}')

