import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

#Plotting a Distplot Without the Histogram

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

sns.distplot([0, 1, 2, 3, 4, 5], kde=False)
plt.show()

#Generate a random normal distribution of size 2x3
x = random.normal(size=(2,3))
print(x)

#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

#Visualization of Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

