from pandas import *
from question import questions_settings, yesOrNo
from pandas import DataFrame
import matplotlib.pyplot as plt


base = read_excel("src/files/BASE.xlsx", sheet_name="DB", index_col=0, header=0)

base_headers = list(base.columns.values)
settings = questions_settings(base_headers)
print(settings)


def create_table_qualitative(column: str, ordinal: bool):
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
        if settings["percentage"] == True:
            relative[key] = "{:.0%}".format(v)
        else:
            relative[key] = v

        if ordinal == True:
            absoluteAcum[key] = val + oldAbsolute
            oldAbsolute += val

            relAcumCurrent = v + oldRelative

            if settings["percentage"] == True:
                relativeAcum[key] = "{:.0%}".format(relAcumCurrent)
            else:
                relativeAcum[key] = relAcumCurrent

            oldRelative += v

            d["Frec. Absoluta Acum"] = absoluteAcum
            d["Frec. Relativa Acum"] = relativeAcum

    table = DataFrame(d, index=index)
    table.index.names = ["Marca de clase"]

    return table


for i in settings["qualitative"]:
    nominal = settings["qualitative"][i]
    t = create_table_qualitative(i, not nominal)

    print("\n Tabla de frecuencias de " + i)
    print(t)

    # t.plot(title="Random")
    # plt.show()
