from pandas import DataFrame


def kurtosis_grouped(Table: DataFrame, n: int, S: float):
    sum_product = 0
    for i in range(1, len(Table) + 1):
        product = (
            Table["MC-Promedi"].get(i)
            * Table["MC-Promedi"].get(i)
            * Table["MC-Promedi"].get(i)
            * Table["MC-Promedi"].get(i)
            * Table["Frec.Absoluta"].get(i)
        )
        sum_product += product

    return sum_product / (n * (S**4))
