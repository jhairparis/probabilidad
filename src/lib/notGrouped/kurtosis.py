from pandas import DataFrame


def kurtosis_no_grouped(base: DataFrame, column: str):
    return base[column].kurt()
