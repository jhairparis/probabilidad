from pandas import DataFrame


def no_grouped_data_average(base: DataFrame, column: str):
    return base[column].sum() / base[column].count()
