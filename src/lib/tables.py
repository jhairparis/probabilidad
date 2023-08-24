from pandas import DataFrame
from lib.grouped.average import grouped_data_average
from lib.grouped.deviation import create_table_deviation_grouped
from lib.grouped.mc_promedi import add_column_mc_promedi
from lib.notGrouped.average import no_grouped_data_average
from lib.notGrouped.deviation import deviation_population, deviation_sample
from lib.notGrouped.geometric_mean import geometric_mean_no_grouped
from lib.notGrouped.harmonic_mean import harmonic_mean_no_grouped
from question import yesOrNo
from math import log10


def percentage_view(val, settings):
    if settings["percentage"] == True:
        return "{:.0%}".format(val)
    else:
        return val


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


def create_table_quantitative(column: str, grouped: bool, base, settings):
    # init vars
    n = base[column].count()
    category = int(round(1 + 3.32 * log10(n), 0))
    min = base[column].min()
    max = base[column].max()
    range_ = max - min
    amplitude = range_ / category * (1 + 0.001)

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
        row.append(percentage_view(freRel, settings))

        freAbsAcum = freAbs + freAbsAcumOld
        row.append(freAbsAcum)

        freRelAcum = freRel + freRelAcumOld
        row.append(percentage_view(freRelAcum, settings))

        li = ls
        freAbsAcumOld = freAbsAcum
        freRelAcumOld = freRelAcum

        d.append(row)

    table = DataFrame(d, index=range(1, category + 1), columns=headers)

    if grouped == True:
        average_grouped = grouped_data_average(table, base, column)
        add_column_mc_promedi(table, average_grouped)

        print("Promedio datos agrupados de {}: {}".format(column, average_grouped))

        print("Tabla de Desviacion de {} agrupados".format(column))
        print(create_table_deviation_grouped(table, base, column, average_grouped))

        return table

    average_no_grouped = no_grouped_data_average(base, column)

    print("Promedio datos de {} no agrupados: {}\n".format(column, average_no_grouped))

    harmonic_mean = harmonic_mean_no_grouped(base, column)

    print("Media armonica de {} no agrupados: {}\n".format(column, harmonic_mean))

    geometric_mean = geometric_mean_no_grouped(base, column)

    print("Media geometrica de {} no agrupados: {}\n".format(column, geometric_mean))

    print("Desviacion de {} no agrupados tipo muestral".format(column))
    print(deviation_sample(base, column))

    print("Desviacion de {} no agrupados tipo poblacional".format(column))
    print(deviation_population(base, column))

    return table
