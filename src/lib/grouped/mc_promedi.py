from pandas import DataFrame


def add_column_mc_promedi(Table: DataFrame,average_grouped):
    row = []
    for i in range(1, len(Table) + 1):
        row.append(pow(Table["MarcaClase"].get(i) - average_grouped, 1))

    Table["MC-Promedi"] = row

