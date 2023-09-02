from pandas import DataFrame
from lib.percentage_view import percentage_view
from question import yesOrNo


def create_table_qualitative(column: str, ordinal: bool, base, settings):
    total_frec_absoluta = base[column].count()
    absolute = base[column].value_counts()
    index = absolute.keys()

    if ordinal == True:
        res = yesOrNo("{} will be ordered ASC(Y) or DESC(N)?".format(column))
        index = index.sort_values(ascending=res)

    relative = {}
    absoluteAcum = {}
    relativeAcum = {}
    d = {
        "Frec. Absoluta": absolute,
        "Frec. Relativa": relative,
    }

    oldAbsolute = 0
    oldRelative = 0
    for key in index:
        val = absolute[key]

        v = val / total_frec_absoluta
        relative[key] = percentage_view(v, settings)

        if ordinal == True:
            absoluteAcum[key] = val + oldAbsolute
            oldAbsolute += val

            relAcumCurrent = v + oldRelative

            relativeAcum[key] = percentage_view(relAcumCurrent, settings)

            oldRelative += v

            d["Frec. Absoluta Acum"] = absoluteAcum
            d["Frec. Relativa Acum"] = relativeAcum

    table = DataFrame(d, index=index)
    table.index.names = ["Marca de clase"]

    return table
