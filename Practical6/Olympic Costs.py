import numpy as np
import matplotlib.pyplot as plt
N = 8
Costs = (1, 8, 15, 7, 5, 14, 43, 40)
#Std = (2, 3, 4, 1, 2, 3, 4, 1)
ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind, Costs, width) #yerr=Std)
plt.ylabel('Costs')
plt.title('Olympic Costs')
plt.xticks(ind, ('LA 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012'))
#plt.yticks(ind, (0, 81, 10))
plt.xticks(fontsize=6)

plt.show()
