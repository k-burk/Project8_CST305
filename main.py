# This code was created by Kara Sumpter
# To generate the graphs for these functions two plots are used
# the one using x and y is used to generate the bar graph that is
# over layed on top of the line graph to show the Reimann sum. X and Y
# are used to generate the line graph using the function from the project instructions.
# To keep the code easier to read I split up the graphs from parts a, b, and c into separate files.

import math
import matplotlib.pyplot as plt
import numpy as np
from Part1c1 import rightHandln
from Part1c2 import rightHandx2
from Part1b import rightHand3x
from Part2 import rightHandExperiment

# defining endpoints
a = -math.pi
b = math.pi
# number of partitions
N = 4

# used to calculate endpoints
x = np.linspace(a, b, N + 1)
y = []
for i in x:
    y.append(math.sin(i) + 1)

# creating the graph
X = np.linspace(a, b)
Y = []
for i in X:
    Y.append(math.sin(i) + 1)

# making sure the subplots are large enough
plt.figure(figsize=(15, 5))

# left endpoints subplot
plt.subplot(1, 3, 1)
plt.plot(X, Y, 'b')
#calculating where on the line the partition should be
x_left = x[:-1]  # Left endpoints
y_left = y[:-1]
plt.plot(x_left, y_left, 'b.', markersize=10)
plt.bar(x_left, y_left, width=(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Left Riemann Sum, N = {}'.format(N))

# midpoint subplot
plt.subplot(1, 3, 2)
plt.plot(X, Y, 'b')
#calculating where on the line the partition should be
# mid finds the average so they are divided by 2
x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
y_mid = []
for i in x_mid:
    y_mid.append(math.sin(i) + 1)
plt.plot(x_mid, y_mid, 'b.', markersize=10)
plt.bar(x_mid, y_mid, width=(b - a) / N, alpha=0.2, edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))

# right endpoints subplot
plt.subplot(1, 3, 3)
plt.plot(X, Y, 'b')
#calculating where on the line the partition should be
x_right = x[1:]  # Right endpoints
y_right = y[1:]
plt.plot(x_right, y_right, 'b.', markersize=10)
plt.bar(x_right, y_right, width=-(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Right Riemann Sum, N = {}'.format(N))

# calculating the values of the Riemann sums
dx = (b-a)/N  # calculating the average of the partitions
x_left = np.linspace(a,b-dx,N)  # calculating the width of each of the bars
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)
# calculating the height for the bars generated
arr = []
for i in x_left:
    arr.append(math.sin(i) + 1)

print("Reimann Sum of sin(x) + 1 with",N,"subintervals.")
left_riemann_sum = np.sum(arr * int(dx)) # adding the area of the bars together
print("Left Riemann Sum:",left_riemann_sum)

arr1 = []
for i in x_midpoint:
    arr1.append(math.sin(i) + 1)
midpoint_riemann_sum = np.sum(x_midpoint * int(dx)) # adding the area of the bars together
print("Midpoint Riemann Sum:",midpoint_riemann_sum)

arr2 = []
for i in x_right:
    arr2.append(math.sin(i) + 1)
right_riemann_sum = np.sum(x_right * int(dx)) # adding the area of the bars together
print("Right Riemann Sum:",right_riemann_sum)


# calling other graph functions for parts b and c
rightHand3x(0, 1, 10)
rightHandln(1, math.e, 10)
rightHandx2(-1, 0, 100)
rightHandExperiment(0, 30, 30)


plt.show()
