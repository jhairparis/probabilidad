from lib.quantitative.grouped.run import run_grouped_data_info
from lib.quantitative.notGrouped.run import run_no_grouped_data_info
from lib.read_file import read_excel
from lib.quantitative.main import create_table_quantitative
from lib.qualitative.main import create_table_qualitative
from lib.user_cli import UserCLI


def manage_qualitative(columns, data, cli: UserCLI):
    print("Varibles cualitativas\n")
    for column in columns:
        nominal = columns[column]
        table = create_table_qualitative(column, not nominal, data, cli)

        print("\n Tabla de frecuencias de " + column)
        print(table)


exit = False
cli = UserCLI()
excel_table = read_excel(cli)

while not exit:
    cli.init(excel_table)

    manage_qualitative(cli.answers["qualitative"], excel_table["data"], cli)

    if len(cli.answers["qualitative"]) > 0:
        print("\n------------\n")
        print("Varibles cuantitativas\n")

    # manage columns quantitative
    for column in cli.answers["quantitative"]:
        grouped = cli.answers["quantitative"][column]
        table, main_values = create_table_quantitative(column, excel_table["data"], cli)

        print("\n Tabla de frecuencias de " + column)
        print(table)

        print(
            "\n ⚠️ El grupo dado es encontrado entre el Li y Ls de la tabla de frecuencia ⚠️ \n"
        )

        if grouped:
            run_grouped_data_info(
                table,
                excel_table["data"],
                column,
                main_values["n"],
                main_values["amplitude"],
                cli,
            )
        else:
            run_no_grouped_data_info(
                table,
                excel_table["data"],
                column,
                main_values["min"],
                main_values["max"],
                cli,
            )

    exit = cli.yesOrNo("¿Desea salir?")
