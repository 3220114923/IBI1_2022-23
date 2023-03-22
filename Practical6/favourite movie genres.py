# A dictionary containing the information in the surey table
sizes = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}
print(sizes)

# Opening a pie chart
import matplotlib.pyplot as plt

# Setting the parameters of the pie chart
labels = ('Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War')
sizes = list(sizes. values()) 
explode = (0,0,0,0,0,0,0,0,0.1,0)

# Creating a pie chart
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

# Inputing the title of pie chart
plt.title('College students favourite movie genres')

# Showing the pie chart
plt.show()
