from pandas import DataFrame


def median_grouped(table: DataFrame, amplitud, media):
    faacmed = 0
    licmed = 0
    fcmed = 0

    findFaacmed = False

    for i in range(1, len(table) + 1):
        if table["Frec.Absoluta.Acum"].get(i) - media >= 0 and findFaacmed == False:
            if table["Frec.Absoluta.Acum"].get(i - 1):
                faacmed = table["Frec.Absoluta.Acum"].get(i - 1)
            licmed = table["Li"].get(i)
            fcmed = table["Frec.Absoluta"].get(i)
            findFaacmed = True

    return licmed + amplitud * ((media - faacmed) / fcmed)
