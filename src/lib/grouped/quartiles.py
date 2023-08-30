from pandas import DataFrame


def quartiles_grouped(table: DataFrame, base: DataFrame, column: str, amplitude):
    Q = []
    cluster = []
    li = []
    a = [amplitude, amplitude, amplitude]
    frecAbsAcumAnter = []
    frecAbso = []

    data = {
        "Q": Q,
        "Grupo": cluster,
        "Li": li,
        "i=a": a,
        "FrecAbsAcumAnter": frecAbsAcumAnter,
        "Frec.Abso": frecAbso,
    }

    Q.append((base[column].count() + 1) / 4)
    Q.append((base[column].count() + 1) / 2)
    Q.append(3 * (base[column].count() + 1) / 4)

    valid = [False, False, False]
    for i in range(1, len(table) + 1):
        if table["Frec.Absoluta.Acum"].get(i) >= Q[0] and not valid[0]:
            cluster.append(i)
            li.append(table["Li"].get(i))
            if table["Frec.Absoluta.Acum"].get(i - 1):
                frecAbsAcumAnter.append(table["Frec.Absoluta.Acum"].get(i - 1))
            else:
                frecAbsAcumAnter.append(0)
            frecAbso.append(table["Frec.Absoluta"].get(i))
            valid[0] = True

        if table["Frec.Absoluta.Acum"].get(i) >= Q[1] and not valid[1]:
            cluster.append(i)
            li.append(table["Li"].get(i))
            if table["Frec.Absoluta.Acum"].get(i - 1):
                frecAbsAcumAnter.append(table["Frec.Absoluta.Acum"].get(i - 1))
            else:
                frecAbsAcumAnter.append(0)
            frecAbso.append(table["Frec.Absoluta"].get(i))
            valid[1] = True

        if table["Frec.Absoluta.Acum"].get(i) >= Q[2] and not valid[2]:
            cluster.append(i)
            li.append(table["Li"].get(i))
            if table["Frec.Absoluta.Acum"].get(i - 1):
                frecAbsAcumAnter.append(table["Frec.Absoluta.Acum"].get(i - 1))
            else:
                frecAbsAcumAnter.append(0)
            frecAbso.append(table["Frec.Absoluta"].get(i))
            valid[2] = True

    res = DataFrame(data)

    q1 = res["Li"].get(0) + res["i=a"].get(0) * (
        res["Q"].get(0) - res["FrecAbsAcumAnter"].get(0)
    ) / res["Frec.Abso"].get(0)

    q2 = res["Li"].get(1) + res["i=a"].get(1) * (
        res["Q"].get(1) - res["FrecAbsAcumAnter"].get(1)
    ) / res["Frec.Abso"].get(1)

    q3 = res["Li"].get(2) + res["i=a"].get(2) * (
        res["Q"].get(2) - res["FrecAbsAcumAnter"].get(2)
    ) / res["Frec.Abso"].get(2)

    return {"q1": q1, "q2": q2, "q3": q3, "table_quartiles": res}
