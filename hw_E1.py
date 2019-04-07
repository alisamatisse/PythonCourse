import matplotlib.pyplot as plt
import numpy as np
s = np.random.poisson(3, 5000)
y = []
for i in s:
    p = (list(s)).count(i)/len(s)
    y.append(p)
plt.scatter(s, y)
plt.xlabel('Random number from distribution')
plt.ylabel("Number's occurence")
plt.title('Poisson distribution')
plt.show()
