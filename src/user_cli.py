import inquirer


class UserCLI:
    answers = {"qualitative": {}, "quantitative": {}}

    def init(self, headers: list):
        q = inquirer.prompt(
            [
                inquirer.Checkbox(
                    "qualitative",
                    message="Seleciona las columnas de tipo cualitativa",
                    choices=headers,
                )
            ]
        )

        for value in q["qualitative"]:
            subQ = inquirer.prompt(
                [
                    inquirer.List(
                        value,
                        message=f"¿La variable {value} es nominal o ordinal?",
                        choices=["Nominal", "Ordinal"],
                        default="Nominal",
                    ),
                ]
            )
            if subQ[value] == "Nominal":
                self.answers["qualitative"][value] = True
            else:
                self.answers["qualitative"][value] = False

            headers.remove(value)

        if len(headers) > 0:
            q2 = inquirer.prompt(
                [
                    inquirer.Checkbox(
                        "quantitative",
                        message="Seleciona las columnas de tipo Cuantitativa",
                        choices=headers,
                    )
                ]
            )

            for value in q2["quantitative"]:
                subQ2 = inquirer.prompt(
                    [
                        inquirer.List(
                            value,
                            message=f"¿La variable {value} la desea analizar de manera agrupada o no agrupada?",
                            choices=["Agrupada", "No agrupada"],
                            default="Agrupada",
                        ),
                    ]
                )
                if subQ2[value] == "Agrupada":
                    self.answers["quantitative"][value] = True
                else:
                    self.answers["quantitative"][value] = False

        q3 = inquirer.prompt(
            [
                inquirer.List(
                    "percentage",
                    message="¿Como desea ver los porcentajes?",
                    choices=["decimal", "%"],
                    default="decimal",
                ),
                inquirer.Confirm(
                    "view_moustache",
                    message="Desea generar la grafica de bigotes cuando sea posible?",
                    default=False,
                    ignore=lambda x: x["percentage"] == "%",
                ),
            ]
        )

        if q3["percentage"] == "decimal":
            self.answers["percentage"] = False
        else:
            self.answers["percentage"] = True

        self.answers["view_moustache"] = q3["view_moustache"]

    def yesOrNo(self, message: str):
        q = [
            inquirer.Confirm("answer", message=message, default=True),
        ]
        return inquirer.prompt(q)["answer"]

    def get_path(self, msg: str):
        print(
            "(Recuerda que la hoja del excel se debe llamar DB y tener la columna indice en la columna A)"
        )
        return inquirer.prompt(
            [
                inquirer.Path(
                    "excel_file",
                    message=msg,
                    exists=True,
                    path_type=inquirer.Path.FILE,
                )
            ]
        )["excel_file"]
