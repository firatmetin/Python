import sys
import os
import math
import matplotlib.pyplot as plt


x = [0, 220, 250, 290, 290, 315]
y = [0, 350, 410, 410, 410, 350]

# plotting the x-axis
plt.plot(x)
# plotting the y-axis
plt.plot(y)
# plot the x-label
plt.xlabel('Horsepower(hp)')
# plot the y-label
plt.ylabel('Torque(nm)')
#title
plt.title('Torque curve')
#spawn the graph
plt.show()
