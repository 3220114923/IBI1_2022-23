# Starting a chart
import numpy as np
import matplotlib.pyplot as plt

N = 8
# Storing the Costs in a list
Costs = (1, 8, 15, 7, 5, 14, 43, 40)
# Leting x locate in groups
ind = np.arange(N)
# Inputing the width of the bar
width = 0.35
# Creating a bar chart
p1 = plt.bar(ind, Costs, width) #yerr=Std)
# Setting parameters
plt.ylabel('Costs')
plt.title('Olympic Costs')
plt.xticks(ind, ('LA 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012'))
plt.xticks(fontsize=6)

# Show the bar chart
plt.show()
