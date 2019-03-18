
# coding: utf-8

# In[105]:


mature = 1
young = 1
#f(n) = f(n-2)*k+f(n-1)
def fib(n, k):
    global mature, young    
    if n > 2:
        young = fib(n-1, k)+fib(n-2, k)*k
        return young
    else:
        young = 1
        return young
    print(young)
fib(36, 4)

