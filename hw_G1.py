
# coding: utf-8

# In[21]:


def logger(func):
    def wrapped(x):
        with open('{}.txt'.format(func.__name__), 'w') as file:
            file.write('{}'.format(func(x)))
        return file
    return wrapped
        
@logger
def multiply_by_two(x):
    return x*2

multiply_by_two(1)

