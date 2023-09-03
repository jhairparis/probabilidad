from pandas import DataFrame


def mode_grouped(Table: DataFrame, amplitude: float):
    d1 = 0
    d2 = 0
    licmod = 0
    for i in range(1, len(Table) + 1):
        if Table["Frec.Absoluta"].get(i) == Table["Frec.Absoluta"].max():
            licmod = Table["Li"].get(i)
            less = 0
            add = 0
            if Table["Frec.Absoluta"].get(i - 1):
                less = Table["Frec.Absoluta"].get(i - 1)
            if Table["Frec.Absoluta"].get(i + 1):
                add = Table["Frec.Absoluta"].get(i + 1)

            d1 = Table["Frec.Absoluta"].get(i) - less
            d2 = Table["Frec.Absoluta"].get(i) - add
            break

    return licmod + amplitude * (d1 / (d1 + d2))
