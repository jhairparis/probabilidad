from pandas import DataFrame
from lib.quantitative.grouped.average import grouped_data_average
from lib.quantitative.grouped.cv import cv_grouped
from lib.quantitative.grouped.deviation import create_table_deviation_grouped
from lib.quantitative.grouped.kurtosis import kurtosis_grouped
from lib.quantitative.grouped.mc_promedi import add_column_mc_promedi
from lib.quantitative.grouped.median_data import median_grouped
from lib.quantitative.grouped.mode_data import mode_grouped
from lib.quantitative.grouped.quartiles import RIC_grouped, quartiles_grouped
from lib.quantitative.grouped.skew import (
    skew_bowley_grouped,
    skew_fisher_grouped,
    skew_person_grouped,
)
from lib.percentage_view import percentage_view
from lib.search_group import search_group
from lib.user_cli import UserCLI


def run_grouped_data_info(
    table: DataFrame,
    base: DataFrame,
    column: str,
    n: int,
    amplitude: float,
    cli: UserCLI,
):
    average_grouped = grouped_data_average(table, base, column)

    print(
        f"Promedio de {column} agrupados: {average_grouped} en el grupo: {search_group(table,average_grouped)}\n"
    )

    add_column_mc_promedi(table, average_grouped)

    if n % 2 == 0:
        media = int(n / 2)
    else:
        media = int((n / 2) + 1)

    print(
        f"Media de {column} agrupados: {media} en el grupo: {search_group(table,media)}\n"
    )

    median__grouped = median_grouped(table, amplitude, media)

    print(
        f"Mediana de {column} agrupados: {median__grouped} en el grupo: {search_group(table,median__grouped)}\n"
    )

    mode__grouped = mode_grouped(table, amplitude)

    print(
        f"Moda de {column} agrupados: {mode__grouped} en el grupo: {search_group(table,mode__grouped)}\n"
    )

    quartiles__grouped = quartiles_grouped(table, base, column, amplitude)

    print(f"Tabla de cuartiles de {column} agrupados")
    print(quartiles__grouped["table_quartiles"])

    RIC__grouped = RIC_grouped(quartiles__grouped["q1"], quartiles__grouped["q3"])

    print(f"RIC de {column} agrupados: {RIC__grouped}")

    print(f"Cuartil Q1 de {column} agrupados: {quartiles__grouped['q1']}")
    print(f"Cuartil Q2 de {column} agrupados: {quartiles__grouped['q2']}")
    print(f"Cuartil Q3 de {column} agrupados: {quartiles__grouped['q3']}\n")

    deviation_grouped = create_table_deviation_grouped(
        table, base, column, average_grouped
    )

    print(f"Tabla de Desviacion de {column} agrupados")
    print(deviation_grouped["table"])

    print(f"Desviacion de {column} agrupados: {deviation_grouped['value']}\n")

    cv__grouped = cv_grouped(deviation_grouped["value"], average_grouped)

    print(
        f"Coeficiente de variacion de {column} agrupados: {percentage_view(cv__grouped,cli)}\n"
    )

    skew_fisher__grouped = skew_fisher_grouped(table, n, deviation_grouped["value"])

    print(f"Asimetria Fisher de {column} agrupados: {skew_fisher__grouped}\n")

    skew_person__grouped = skew_person_grouped(
        average_grouped, mode__grouped, deviation_grouped["value"]
    )

    print(f"Asimetria Person de {column} agrupados: {skew_person__grouped}\n")

    skew_bowley__grouped = skew_bowley_grouped(
        quartiles__grouped["q1"], quartiles__grouped["q2"], quartiles__grouped["q3"]
    )

    print(f"Asimetria Bowley de {column} agrupados: {skew_bowley__grouped}\n")

    kurtosis__grouped = kurtosis_grouped(table, n, deviation_grouped["value"])

    print(f"Curtosis de {column} agrupados: {kurtosis__grouped}\n")
