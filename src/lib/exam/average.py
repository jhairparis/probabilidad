from pandas import DataFrame

from lib.notGrouped.average import no_grouped_data_average


def average_all(base: DataFrame, data: str):
    if len(data["colum_average_simple"]) > 0:
        print(
            f"Promedio simple de {data['colum_average_simple'][0]}: ",
            no_grouped_data_average(base, data["colum_average_simple"][0]),
        )

    if len(data["columns_average_weighted"]) > 0:
        print(
            "Promedio ponderado",
            average_weighted(
                base,
                data["columns_average_weighted"][0],
                data["columns_average_weighted"][1],
                data["main_average_weighted"][0],
            ),
        )

    return


def average_weighted(base: DataFrame, colum1, colum2, column_main):
    sum_product = 0

    for i in base.index:
        product = base[colum1].get(i) * base[colum2].get(i)
        sum_product += product

    return sum_product / base[column_main].sum()
