
# coding: utf-8

# In[21]:


with open('C:\\Users\\Alice Aspire\\Desktop\\биоинформатика\\python data\\rosalind_revc.txt') as file:
    dna = file.read()
    print(dna)
    dna = dna.replace('A', 'X').replace('C', 'Y').replace('T', 'A').replace('G', 'C')
    dna = dna.replace('X', 'T').replace('Y', 'G')[::-1]
    print(dna)

