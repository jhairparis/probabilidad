from pandas import DataFrame


def mode_grouped(table: DataFrame, amplitude):
    d1 = 0
    d2 = 0
    licmod = 0
    for i in range(1, len(table) + 1):
        if table["Frec.Absoluta"].get(i) == table["Frec.Absoluta"].max():
            licmod = table["Li"].get(i)
            less = 0
            add = 0
            if table["Frec.Absoluta"].get(i - 1):
                less = table["Frec.Absoluta"].get(i - 1)
            if table["Frec.Absoluta"].get(i + 1):
                add = table["Frec.Absoluta"].get(i + 1)

            d1 = table["Frec.Absoluta"].get(i) - less
            d2 = table["Frec.Absoluta"].get(i) - add
            break

    return licmod + amplitude * (d1 / (d1 + d2))
