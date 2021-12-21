import matplotlib.pyplot as plt
import numpy as np

# a and b are endpoints, N is number of partitions
def rightHandExperiment(a, b, N):
    # used to calculate endpoints
    x = np.linspace(a, b, N + 1)
    y = []
    for i in x:
        y.append(1.69 + 0.0275*i + .00093*i*i - .0000382*i*i*i)

    # creating the graph
    X = np.linspace(a, b)
    Y = []
    for i in X:
        Y.append(1.69 + 0.0275*i + .00093*i*i - .0000382*i*i*i)

    # making sure the subplots are large enough
    plt.figure(figsize=(15, 5))

    # right endpoints plot
    plt.plot(X, Y, 'b')
    x_right = x[1:]  # Right endpoints
    y_right = y[1:]
    plt.plot(x_right, y_right, 'b.', markersize=10)
    plt.bar(x_right, y_right, width=-(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Right Riemann Sum 3x+2x^2, N = {}'.format(N))

    # calculating the values of the Riemann sums
    dx = (b - a) / N  # calculating the average of the partitions
    x_right = np.linspace(dx, b, N) # calculating the width of each of the bars
    arr = []
    for i in x_right:     # calculating the height for the bars generated
        arr.append(1.69 + 0.0275*i + .00093*i*i - .0000382*i*i*i)

    print("Reimann Sum of  with", N, "subintervals.")
    right_riemann_sum = np.sum(arr * int(dx))  # adding the area of the bars together
    print("Right Riemann Sum:", right_riemann_sum)

