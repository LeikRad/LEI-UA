import matplotlib.pyplot as plt
import numpy as np
import math    

circle2 = plt.Circle((0, 0), 0.170, fill = False)
circle3 = plt.Circle((0, 0), 0.162, fill = False)
circle4 = plt.Circle((0, 0), 0.107, fill = False)
circle5 = plt.Circle((0, 0), 0.099, fill = False)
circle6 = plt.Circle((0, 0), 0.032, fill = False)
circle7 = plt.Circle((0, 0), 0.0127, fill = False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(circle4)
ax.add_patch(circle5)
ax.add_patch(circle6)
ax.add_patch(circle7)

i = 0
while (i <= 180):
    x1 = 0
    y1 = 0
    angle = i

    sl = np.tan(np.radians(angle))

    plt.axline((x1,y1), slope=sl)
    i = i + 9

plt.plot([0.150], [0.020], marker='o', markersize=3, color="red")

plt.show()
