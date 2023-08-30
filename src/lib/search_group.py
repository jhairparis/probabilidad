from pandas import DataFrame


def search_group(table: DataFrame, value):
    group_find = -1
    for i in range(1, len(table) + 1):
        if value >= table["Li"].get(i) and value <= table["Ls"].get(i):
            group_find = i

    return group_find
