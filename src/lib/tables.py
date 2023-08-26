from pandas import DataFrame
from lib.grouped.average import grouped_data_average
from lib.grouped.deviation import create_table_deviation_grouped
from lib.grouped.mc_promedi import add_column_mc_promedi
from lib.grouped.median_data import median_grouped
from lib.grouped.mode_data import mode_grouped
from lib.notGrouped.average import no_grouped_data_average
from lib.notGrouped.deviation import deviation_population, deviation_sample
from lib.notGrouped.geometric_mean import geometric_mean_no_grouped
from lib.notGrouped.harmonic_mean import harmonic_mean_no_grouped
from lib.notGrouped.median_data import median_no_grouped
from lib.notGrouped.mode_data import mode_no_grouped
from lib.notGrouped.quartiles import Q1, Q2, Q3, view_graph_moustache
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

        print(f"Promedio de {column} agrupados: {average_grouped}\n")

        add_column_mc_promedi(table, average_grouped)

        if n % 2 == 0:
            media = int(n / 2)
        else:
            media = int((n / 2) + 1)

        print(f"Media de {column} agrupados: {media}\n")

        median__grouped = median_grouped(table, amplitude, media)

        print(f"Mediana de {column} agrupados: {median__grouped}\n")

        mode__grouped = mode_grouped(table, amplitude)

        print(f"Moda de {column} agrupados: {mode__grouped}\n")

        print(f"Tabla de Desviacion de {column} agrupados")
        print(create_table_deviation_grouped(table, base, column, average_grouped))

        return table

    average_no_grouped = no_grouped_data_average(base, column)

    print(f"Promedio datos de {column} no agrupados: {average_no_grouped}\n")

    harmonic_mean = harmonic_mean_no_grouped(base, column)

    print(f"Media armonica de {column} no agrupados: {harmonic_mean}\n")

    geometric_mean = geometric_mean_no_grouped(base, column)

    print(f"Media geometrica de {column} no agrupados: {geometric_mean}\n")

    median_no__grouped = median_no_grouped(base, column)

    print(f"Mediana de {column} no agrupados: {median_no__grouped}\n")

    mode_no__grouped = mode_no_grouped(base, column)

    print(f"Moda de {column} no agrupados: {mode_no__grouped}\n")

    deviation_s = deviation_sample(base, column)

    print(f"Desviacion de {column} no agrupados tipo muestral: {deviation_s}\n")

    deviation_p = deviation_population(base, column)

    print(f"Desviacion de {column} no agrupados tipo poblacional: {deviation_p}\n")

    q1 = Q1(base, column)
    q2 = Q2(base, column)
    q3 = Q3(base, column)

    print(f"Cuartil Q1 de {column} no agrupados: {q1}")
    print(f"Cuartil Q2 de {column} no agrupados: {q2}")
    print(f"Cuartil Q3 de {column} no agrupados: {q3}")

    if settings["view_moustache"] == True:
        info = {
            "median": median_no__grouped,
            "q1": q1,
            "q3": q3,
            "minimum": min,
            "maximum": max,
            "mean": average_no_grouped,
        }

        view_graph_moustache(base, column, info)

    return table
