from pandas import DataFrame
from lib.percentage_view import percentage_view
from math import log10
from user_cli import UserCLI


def create_table_quantitative(column: str, base: DataFrame, cli: UserCLI):
    # init vars
    n = base[column].count()
    category = int(round(1 + 3.32 * log10(n), 0))
    min = base[column].min()
    max = base[column].max()
    range_ = max - min
    amplitude = range_ / category * (1 + 0.001)

    print(f"n: {n}")
    print(f"categorias/sturges: {category}")
    print(f"min: {min}")
    print(f"max: {max}")
    print(f"rango: {range_}")
    print(f"amplitud/intervalo de la clase: {amplitude}\n")

    # ---
    d = []
    headers = [
        "Li",
        "Ls",
        "MarcaClase",
        "Frec.Absoluta",
        "Frec.Relativa",
        "Frec.Absoluta.Acum",
        "Frec.Relative.Acum",
    ]

    li = min
    freAbsAcumOld = 0
    freRelAcumOld = 0
    for i in range(category):
        row = []
        ls = li + amplitude
        row.append(li)
        row.append(ls)
        row.append((li + ls) / 2)

        freAbs = base[column][base[column].between(li, ls)].count()
        row.append(freAbs)

        freRel = freAbs / n
        row.append(percentage_view(freRel, cli))

        freAbsAcum = freAbs + freAbsAcumOld
        row.append(freAbsAcum)

        freRelAcum = freRel + freRelAcumOld
        row.append(percentage_view(freRelAcum, cli))

        li = ls
        freAbsAcumOld = freAbsAcum
        freRelAcumOld = freRelAcum

        d.append(row)

    table = DataFrame(d, index=range(1, category + 1), columns=headers)

    return table, {
        "n": n,
        "category": category,
        "min": min,
        "max": max,
        "range_": range_,
        "amplitude": amplitude,
    }
