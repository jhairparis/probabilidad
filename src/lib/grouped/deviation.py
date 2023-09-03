from math import sqrt
from pandas import DataFrame


def create_table_deviation_grouped(
    Table: DataFrame, base: DataFrame, column: str, average_grouped: float
):
    sumProduct = 0
    total = Table["Frec.Absoluta"].sum()
    for i in range(1, len(Table) + 1):
        product = (
            Table["Frec.Absoluta"].get(i)
            * Table["MC-Promedi"].get(i)
            * Table["MC-Promedi"].get(i)
        )
        sumProduct += product

    deviation = sqrt(sumProduct / (total - 1))

    d = []
    headers = [
        "-3S",
        "-2S",
        "-S",
        "x",
        "S",
        "2S",
        "3S",
    ]

    n3S = average_grouped - (3 * deviation)
    n2S = average_grouped - (2 * deviation)
    nS = average_grouped - deviation

    pS = average_grouped + deviation
    p2S = average_grouped + (2 * deviation)
    p3S = average_grouped + (3 * deviation)

    d.append(
        [
            n3S,
            n2S,
            nS,
            (base[column] < pS).sum() - (base[column] < nS).sum(),
            pS,
            p2S,
            p3S,
        ]
    )
    d.append(
        [
            0,
            0,
            0,
            (base[column] < p2S).sum() - (base[column] < n2S).sum(),
            0,
            0,
            0,
        ]
    )
    d.append(
        [
            0,
            0,
            0,
            (base[column] < p3S).sum() - (base[column] < n3S).sum(),
            0,
            0,
            0,
        ]
    )

    DeviationTable = DataFrame(d, index=[1, 2, 3], columns=headers)

    return {"table": DeviationTable, "value": deviation}
