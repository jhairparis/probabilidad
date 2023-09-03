from pandas import DataFrame


def mode_no_grouped(base: DataFrame, column: str):
    return base[column].mode().get(0)
