
# coding: utf-8

# In[18]:


with open('C:\\Users\\Alice Aspire\\Desktop\\биоинформатика\\python data\\rosalind_hamm.txt') as file:
    a = file.read()
    a = a.split('\n')
    dna1 = a[0]
    dna2 = a[1]
    dna3 = []
    dna4 = []
    print(dna1)
    count = 0
    i, j = 0, 0
    for char in dna1:
        dna3 += char
    for char in dna2:
        dna4 += char
    for i in range(len(dna1)):
        if dna3[i] != dna4[j]:
            count+=1
        j+=1
        i+=1
    print(count)          

