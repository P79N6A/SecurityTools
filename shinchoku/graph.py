import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import math
 
plt.style.use('default')
sns.set()
sns.set_style('whitegrid')
sns.set_palette('Set1')
    
x = np.array([00,10,20,30,40,50,60,70,80,90,"A0","B0","C0","D0","E0","F0"])
gene_1 = np.array([402,688,738,451,230,151,145,285,147,121,108,519,287,402,23,21])
gene_2 = np.array([300,604,638,331,436,321,235,285,327,211,248,549,207,422,123,41])
gene_seikika_1 = []
gene_seikika_2 = []

for i in range(0,len(gene_1)):
    gene_seikika_1.append((gene_1[i]-23)/715)
for j in range(0,len(gene_2)):
    gene_seikika_2.append((gene_2[j]-23)/715)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, gene_seikika_1, label='Ransomware')
ax.plot(x, gene_seikika_2, label='subspecies1')


ax.legend()
ax.set_xlabel("Bytecode")
ax.set_ylabel("frequency")
ax.set_ylim(0, 1)

plt.show()
