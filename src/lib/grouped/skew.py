from pandas import DataFrame


def skew_fisher_grouped(Table: DataFrame, n, S):
    sum_product = 0
    for i in range(1, len(Table) + 1):
        product = (
            Table["MC-Promedi"].get(i)
            * Table["MC-Promedi"].get(i)
            * Table["MC-Promedi"].get(i)
            * Table["Frec.Absoluta"].get(i)
        )
        sum_product += product

    return sum_product / (n * (S**3))


def skew_person_grouped(average, mode, S):
    return (average - mode) / S


def skew_bowley_grouped(q1, q2, q3):
    return (q3 + q1 - 2 * q2) / (q3 - q1)
