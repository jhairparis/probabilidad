from lib.notGrouped.average import no_grouped_data_average
from lib.notGrouped.cv import cv_no_grouped
from lib.notGrouped.deviation import deviation_population, deviation_sample
from lib.notGrouped.geometric_mean import geometric_mean_no_grouped
from lib.notGrouped.harmonic_mean import harmonic_mean_no_grouped
from lib.notGrouped.kurtosis import kurtosis_no_grouped
from lib.notGrouped.median_data import median_no_grouped
from lib.notGrouped.mode_data import mode_no_grouped
from lib.notGrouped.quartiles import Q1, Q2, Q3, RIC_no_grouped, view_graph_moustache
from lib.notGrouped.skew import (
    skew_bowley_no_grouped,
    skew_fisher_no_grouped,
    skew_person_no_grouped,
)
from lib.percentage_view import percentage_view
from lib.search_group import search_group


def run_no_grouped_data_info(table, base, column, settings):
    average_no_grouped = no_grouped_data_average(base, column)

    print(
        f"Promedio datos de {column} no agrupados: {average_no_grouped} en el grupo: {search_group(table,average_no_grouped)}\n"
    )

    harmonic_mean = harmonic_mean_no_grouped(base, column)

    print(
        f"Media armonica de {column} no agrupados: {harmonic_mean} en el grupo: {search_group(table,harmonic_mean)}\n"
    )

    geometric_mean = geometric_mean_no_grouped(base, column)

    print(
        f"Media geometrica de {column} no agrupados: {geometric_mean} en el grupo: {search_group(table,geometric_mean)}\n"
    )

    median_no__grouped = median_no_grouped(base, column)

    print(
        f"Mediana de {column} no agrupados: {median_no__grouped} en el grupo: {search_group(table,median_no__grouped)}\n"
    )

    mode_no__grouped = mode_no_grouped(base, column)

    print(
        f"Moda de {column} no agrupados: {mode_no__grouped} en el grupo: {search_group(table,mode_no__grouped)}\n"
    )

    deviation_s = deviation_sample(base, column)

    print(
        f"Desviacion de {column} no agrupados tipo muestral: {deviation_s} en el grupo: {search_group(table,deviation_s)}\n"
    )

    deviation_p = deviation_population(base, column)

    print(
        f"Desviacion de {column} no agrupados tipo poblacional: {deviation_p} en el grupo: {search_group(table,deviation_p)}\n"
    )

    cv_no__grouped = cv_no_grouped(deviation_s, average_no_grouped)

    print(
        f"Coeficiente de variacion de {column} no agrupados: {percentage_view(cv_no__grouped,settings)}\n"
    )

    q1 = Q1(base, column)
    q2 = Q2(base, column)
    q3 = Q3(base, column)

    RIC_no__grouped = RIC_no_grouped(q1, q3)

    print(f"RIC de {column} no agrupados: {RIC_no__grouped}")

    print(f"Cuartil Q1 de {column} no agrupados: {q1}")
    print(f"Cuartil Q2 de {column} no agrupados: {q2}")
    print(f"Cuartil Q3 de {column} no agrupados: {q3}\n")

    skew_fisher_no__grouped = skew_fisher_no_grouped(base, column)

    print(f"Asimetria Fisher de {column} no agrupados: {skew_fisher_no__grouped}\n")

    skew_person_no__grouped = skew_person_no_grouped(
        average_no_grouped, mode_no__grouped, deviation_s
    )

    print(f"Asimetria Person de {column} no agrupados: {skew_person_no__grouped}\n")

    skew_bowley_no__grouped = skew_bowley_no_grouped(q1, q2, q3)

    print(f"Asimetria Bowley de {column} no agrupados: {skew_bowley_no__grouped}\n")

    kurtosis_no__grouped = kurtosis_no_grouped(base, column)

    print(f"Curtosis de {column} no agrupados: {kurtosis_no__grouped}\n")

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
