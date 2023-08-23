from pandas import DataFrame


def deviation_sample(base: DataFrame, column: str):
    return base[column].std()


def deviation_population(base: DataFrame, column: str):
    return base[column].std(ddof=0)
