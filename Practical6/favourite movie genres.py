import matplotlib.pyplot as plt

labels = ('Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War')
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
explode = (0,0,0,0,0,0,0,0,0.1,0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

plt.title('College students favourite movie genres')
plt.show()
