from pandas import DataFrame


def add_column_mc_promedi(Table: DataFrame):
    sumProduct = 0
    total = Table["Frec.Absoluta"].sum()
    for i in range(1, len(Table) + 1):
        product = Table["MarcaClase"].get(i) * Table["Frec.Absoluta"].get(i)
        sumProduct += product

    average_grouped = sumProduct / total

    row = []
    for i in range(1, len(Table) + 1):
        row.append(pow(Table["MarcaClase"].get(i) - average_grouped, 1))

    Table["MC-Promedi"] = row

    return average_grouped
