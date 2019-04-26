
# coding: utf-8

# In[111]:


def prime(start, end):
    current = start
    is_prime = True
    while current < end:
        is_prime = True
        for i in range(2, current):
            if current % i == 0:
                is_prime = False
                break
        if is_prime:
            yield current   
        current += 1
for number in prime(2, 30):
    print(number, end=' ')

