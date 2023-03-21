import numpy as np
import matplotlib.pyplot as plt

N = 10
Number of students = (73, 42, 38, 28, 22, 19, 18, 12, 8, 7)
Std = ()
ind = np.arrange(N)
width = 0.35
p1 = plt.bar(ind,number of students, width, yerr=Std)
plt.ylabel('Number of students')
plt.title('Chinese university students favourite movie genres')
plt.xticks(ind, ('Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War',))
plt.yticks(np.arrange(0, 81,10))

plt.show()

import matplotlib.pyplot as plt

labels = ('Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
explode = (0,0.1,0,0,0,0,0,0,0)
plt.pie(sizes, explede=explode, labels=labels, autopct='1.1f%%', shadow=False, startangle=90)
plt.show()
