from pandas import DataFrame


def skew_fisher_no_grouped(base: DataFrame, column: str):
    return base[column].skew()


def skew_person_no_grouped(average: float, mode: float, S: float):
    return (average - mode) / S


def skew_bowley_no_grouped(q1: float, q2: float, q3: float):
    return (q3 + q1 - 2 * q2) / (q3 - q1)
