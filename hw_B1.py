
# coding: utf-8

# In[ ]:


with open('C:\\Users\\Alice Aspire\\Desktop\\биоинформатика\\python data\\rosalind_rna.txt') as file:
    dna = str(file.read())
    rna = dna.replace('T', 'U')
    print(rna)

