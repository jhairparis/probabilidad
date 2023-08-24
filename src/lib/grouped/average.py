from pandas import DataFrame


def grouped_data_average(Table: DataFrame, base: DataFrame, column: str):
    sum_product = 0
    for i in range(1, len(Table) + 1):
        product = Table["MarcaClase"].get(i) * Table["Frec.Absoluta"].get(i)
        sum_product += product
    return sum_product / base[column].count()
