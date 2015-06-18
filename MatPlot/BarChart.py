import numpy as np
import matplotlib.pyplot as plt


def drawBarChart(label,performance,chartTitle,xLabel):

    x_pos = np.arange(len(label))
    plt.barh(x_pos, performance, align='center', alpha=0.5)
    # Label control
    plt.yticks(x_pos, label)
    plt.xlabel(xLabel)
    plt.title(chartTitle)

    plt.show()
