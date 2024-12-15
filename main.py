# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:59:57 2024

@author: gokul
"""

import pandas as pd

cus=pd.read_csv('shopping_trends.csv')
cus.info()
high=pd.value_counts(cus['Item Purchased'])
high=high.head(10)
import matplotlib.pyplot as plt
plt.pie(high.values,labels=high.index,autopct='%1.1f%%')
plt.title('highest selling product')
plt.show()

prora=cus[['Review Rating','Item Purchased']]
prora=prora.groupby('Item Purchased')['Review Rating'].mean()

plt.figure(figsize=(20,15))
plt.barh(prora.index,prora.values)
plt.yticks(fontsize=20)
plt.title('review of items purchased')
plt.show()
import seaborn as sns

prora=cus[['Category','Season']]
prora=prora.groupby(["Category", "Season"]).size().unstack(fill_value=0)
plt.figure(figsize=(10, 6))
sns.heatmap(prora, annot=True, fmt="d")
plt.title("Frequency of Categories Across Seasons")
plt.show()

loci=cus[['Location','Item Purchased']]
loci=loci.groupby(['Location','Item Purchased']).size().unstack(fill_value=0)
loci.plot(kind='bar',figsize=(20,15))
plt.title('most purchased item by location')
loci.legend()
plt.show()