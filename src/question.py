import inquirer


def questions_settings(headers: list):
    subAns1 = {}
    q = [
        inquirer.Checkbox(
            "qualitative",
            message="Select variables `Cualitativa`",
            choices=headers,
        ),
    ]
    for value in inquirer.prompt(q)["qualitative"]:
        subQ = [
            inquirer.Confirm(
                value,
                message="Is the variable {} `nominal`?".format(value),
                default=True,
            ),
        ]
        subAns1[value] = inquirer.prompt(subQ)[value]
        headers.remove(value)
    ans1 = {"qualitative": subAns1}

    if len(headers) > 0:
        subAns2 = {}
        q2 = inquirer.prompt(
            [
                inquirer.Checkbox(
                    "quantitative",
                    message="Select variables `Cualitativa`",
                    choices=headers,
                )
            ]
        )

        for value in q2["quantitative"]:
            subQ2 = [
                inquirer.Confirm(
                    value,
                    message="Is the variable {} `Discreta`?".format(value),
                    default=True,
                ),
            ]
            subAns2[value] = inquirer.prompt(subQ2)[value]
        ans1["quantitative"] = subAns2

    q3 = [
        inquirer.Confirm(
            "percentage", message="Do you want view 0.19 like 19%?", default=True
        ),
    ]

    ans3 = inquirer.prompt(q3)

    # {qualitative:{key: True == nominal},quantitative:{key: True == Discreta}}
    return dict(ans1, **ans3)

def yesOrNo(message):
    q = [
        inquirer.Confirm(
            "answer", message=message, default=True
        ),
    ]
    return inquirer.prompt(q)["answer"]