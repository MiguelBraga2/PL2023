from matplotlib import pyplot as plt
import numpy as np

def draw_histogram(data, minimum, maximum, delta):
    a = np.array(data)
    fig, ax = plt.subplots()
    ax.hist(a, bins=list(range(minimum, maximum, delta)))
    plt.show()

def draw_pie_plot(percentages):
    labels = 'Masculino', 'Feminino'

    fig, ax = plt.subplots()
    ax.pie(percentages, labels=labels)

    plt.show()
