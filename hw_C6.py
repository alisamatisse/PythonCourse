
# coding: utf-8

# In[92]:


with open('C:\\Users\\Alice Aspire\\Desktop\\биоинформатика\\питон от мехмата 19\\rosalind_subs.txt') as file:
    subs = file.read()
    print(subs)
    subs = subs.split('\n')
    s = subs[0]
    t = subs[1]
    k = len(t)
    m = []
    positions = []
    for i in range(len(s)):
        positions.append(s[i:i+k])
    print(positions)
    for i in range(len(positions)):
        if positions[i] == t:
            m.append(i+1)
    print(' '.join(str(x) for x in m))
        

