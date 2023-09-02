import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


def view_graph_moustache(base: DataFrame, column: str, info: dict):
    _, ax = plt.subplots()
    ax.boxplot(base[column])
    ax.set_title("Grafica de {}".format(column))

    ax.text(1.1, info["median"], f"Mediana: {info['median']:.2f}")
    ax.text(1.1, info["q1"], f"Q1: {info['q1']:.2f}")
    ax.text(1.1, info["q3"], f"Q3: {info['q3']:.2f}")
    ax.text(1.1, info["minimum"], f"Mínimo: {info['minimum']:.2f}")
    ax.text(1.1, info["maximum"], f"Máximo: {info['maximum']:.2f}")
    ax.text(0.5, info["mean"], f'Promedio: {info["mean"]:.2f}')

    plt.show()
    return 0


def Q1(base, column):
    return np.percentile(base[column], 25)


def Q2(base, column):
    return np.percentile(base[column], 50)


def Q3(base, column):
    return np.percentile(base[column], 75)


def RIC_no_grouped(q1, q3):
    return q3 - q1
