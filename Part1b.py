import matplotlib.pyplot as plt
import numpy as np

# a and b are endpoints, N is number of partitions
def rightHand3x(a, b, N):
    # used to calculate endpoints
    x = np.linspace(a, b, N + 1)
    y = []
    for i in x:
        y.append((3*i)+(2*i*i))

    # creating the graph
    X = np.linspace(a, b)
    Y = []
    for i in X:
        Y.append((3*i)+(2*i*i))

    # making sure the subplots are large enough
    plt.figure(figsize=(15, 5))

    # right endpoints plot
    plt.plot(X, Y, 'b')
    x_right = x[1:]  # Right endpoints
    y_right = y[1:]
    plt.plot(x_right, y_right, 'b.', markersize=10)
    plt.bar(x_right, y_right, width=-(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Right Riemann Sum 3x+2x^2, N = {}'.format(N))


