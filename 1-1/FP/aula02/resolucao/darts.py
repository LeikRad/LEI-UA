import math
# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")


x = float(input("x? "))
y = float(input("y? "))
# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...


if (x == 0 and y > 0):
    angle = 0.0
elif(x == 0 and y < 0):
    angle = 180.0
elif(x > 0 and y == 0):
    angle = 90.0
elif(x < 0 and y == 0):
    angle = 270.0
else:
    tempAngle = math.degrees(math.atan(y/x))
    if(x > 0 and y > 0):
        angle = 99.0 - tempAngle
    elif(x > 0 and y < 0):
        angle = 189.0 - tempAngle
    elif(x < 0 and y < 0):
        angle = 279.0 - tempAngle
    elif(x < 0 and y > 0):
        angle = 369.0 - tempAngle

if ((x)**2+(y)**2 >= 170**2):
    score = 0
elif ((x)**2+(y)**2 <= 170**2 and (x)**2+(y)**2 >= 162**2):
    score = POINTS[int(angle // 18)] * 2
elif((x)**2+(y)**2 <= 107**2 and (x)**2+(y)**2 >= 99**2):
    score = POINTS[int(angle // 18)] * 3
elif((x)**2+(y)**2 <= 32**2 and (x)**2+(y)**2 >= 12.7**2):
    score = 25
elif((x)**2+(y)**2 <= 12.7**2):
    score = 50
else:
    score = POINTS[int(angle // 18)]

print(score)


#EXTRA PARA VERIFICAR SE O CODIGO ESTÁ CERTO
import matplotlib.pyplot as plt
import numpy as np

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
    i = i + 18

plt.plot([x/1000], [y/1000], marker='o', markersize=3, color="red")

plt.show()

