from pandas import DataFrame
import numpy as np


def geometric_mean_no_grouped(base: DataFrame, column: str):
    logValor = np.log(base[column])
    return np.exp(np.mean(logValor))
