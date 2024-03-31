### x and y
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
for i in np.arange(0, 3.1, 0.5):
    x.append(i)
    y.append( 64- (16 * (i-1)**2))

plt.title("Time and height")
plt.xlabel("Time")
plt.ylabel("Height")
plt.bar(x, y, color='orange', width = 0.25)
plt.show()    
