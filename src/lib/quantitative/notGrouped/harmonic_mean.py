from pandas import DataFrame


def harmonic_mean_no_grouped(base: DataFrame, column: str):
    return base[column].count() / sum(1 / base[column])
