# What does this piece of code do?
# Answer:

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# Initialize the progress is 0
progress=0
# Initialize the stored_random_number is 0
stored_random_number=0
# limit the progress less then 10
while progress<10:
# Increment the progress count by
        progress+=1
# randint(1,100) draws a randow number between 1 and 100
        n = randint(1,100)
# compare n and the stored_random_number
        if n > stored_random_number:
# let stroed_randem_number be n
	        stored_random_number = n

#print the result
print(stored_random_number)
