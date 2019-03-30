
# coding: utf-8

# In[31]:


def f(x):
    return x*2
b = int(input('Введите верхний предел интегрирования b: '))
a = int(input('Введите нижний предел интегрирования a: '))
n = int(input('Введите число интервалов разбиения N: '))
def rectangular(f, a, b, n):
    '''Считает интеграл методом прямоугольника'''
    h = (b - a)/n
    result = 0
    for i in range(1, n):
        result += f(a + 0.5*h + i*h)
    result *= h
    return result
def Simpson(f, a, b, n):
    '''Считает интеграл методом Симпсона'''
    h = (b - a)/n
    result = f(a)+f(b)
    for i in range(1, n-1):
        result += f(a + i*h)*2
    for i in range(1, n-1):
        result += f(a + 0.5*h + i*h)*4
    result = result*h/6
    return result
Simpson(f, a, b, n)

