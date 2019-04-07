
# coding: utf-8

# In[140]:


import pandas as pd
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
dataset = load_boston()
boston_df = pd.DataFrame(dataset['data'], columns=dataset['feature_names'])
#добавляем столбец со стоимостью
boston_df['PRICE'] = dataset.target
# смотрим, какие данные у нас есть
print ("Columns: " + " ".join (boston_df.columns))
# ищу корреляции методом Пирсона (самый медленный) между всеми переменными
pearson = boston_df.corr(method='pearson')
# из всего этого мне нужна корреляция только CRIME с остальными переменными
corr_with_target = pearson.ix[-1][:-1]
sorted_corr = corr_with_target[abs(corr_with_target).argsort()[::-1]]
#index позволяет взять только имена рядов
plt.figure(figsize=(15,10))
for i in sorted_corr.index[:3]:
    plt.scatter(boston_df["PRICE"], boston_df[i])
attr = ["% lower status of the population", "average number of rooms per dwelling", "pupil-teacher ratio by town"]
plt.legend(attr)
plt.title ("You think this bad neighborhood?")
plt.xlabel ("Price")
plt.ylabel ("Attribute value")
plt.show()

