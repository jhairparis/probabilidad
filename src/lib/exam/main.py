import inquirer
from pandas import DataFrame

from lib.exam.average import average_all


def exam(base: DataFrame, headers: dict):
    res = inquirer.prompt(
        [
            inquirer.Checkbox(
                "column",
                message="Seleciona la columna para el promedio simple: ",
                choices=headers,
            ),
            inquirer.Checkbox(
                "columns",
                message="Seleciona las 2 columnas para el promedio ponderado: ",
                choices=headers,
            ),
            inquirer.Checkbox(
                "main",
                message="A cual columna debe tener presente seleciona 1: ",
                choices=headers,
            ),
        ]
    )
    info = {
        "colum_average_simple": res["column"],
        "columns_average_weighted": res["columns"],
        "main_average_weighted": res["main"],
    }

    average_all(base, info)
