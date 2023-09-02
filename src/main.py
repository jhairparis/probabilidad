from lib.grouped.run import run_grouped_data_info
from lib.notGrouped.run import run_no_grouped_data_info
from lib.read_file import read_excel
from lib.quantitative import create_table_quantitative
from lib.qualitative import create_table_qualitative
from question import questions_settings, yesOrNo


exit = False
while not exit:
    excel_table = read_excel()

    settings = questions_settings(excel_table["headers"])

    for column in settings["qualitative"]:
        nominal = settings["qualitative"][column]
        table = create_table_qualitative(column, not nominal, excel_table["data"], settings)

        print("\n Tabla de frecuencias de " + column)
        print(table)

    print("\n------------\n")

    for column in settings["quantitative"]:
        grouped = settings["quantitative"][column]
        table, main_values = create_table_quantitative(column, excel_table["data"], settings)

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
                settings,
            )
        else:
            run_no_grouped_data_info(table, excel_table["data"], column, settings)

    exit = yesOrNo("Desea salir?")
