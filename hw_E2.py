import numpy as np
import matplotlib.pyplot as plt

s = np.random.pareto(1, 5000)
plt.hist(s, 5000)
plt.xlim(0, 60)
plt.xlabel('Pareto number')
plt.ylabel('Occurence')

plt.show()