import numpy as np
import matplotlib.pyplot as plt
i = 0
while (i <= 180):
    x1 = 0
    y1 = 0
    angle = i

    sl = np.tan(np.radians(angle))

    plt.axline((x1,y1), slope=sl)
    i = i + 9

plt.legend()
plt.grid()
plt.show()
