from pandas import DataFrame


def median_grouped(Table: DataFrame, amplitude: float, media: float):
    faacmed = 0
    licmed = 0
    fcmed = 0

    findFaacmed = False

    for i in range(1, len(Table) + 1):
        if Table["Frec.Absoluta.Acum"].get(i) - media >= 0 and findFaacmed == False:
            if Table["Frec.Absoluta.Acum"].get(i - 1):
                faacmed = Table["Frec.Absoluta.Acum"].get(i - 1)
            licmed = Table["Li"].get(i)
            fcmed = Table["Frec.Absoluta"].get(i)
            findFaacmed = True

    return licmed + amplitude * ((media - faacmed) / fcmed)
