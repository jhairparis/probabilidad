from lib.exam.main import exam
from lib.read_file import read_excel
from lib.tables import create_table_qualitative, create_table_quantitative
from question import questions_settings, yesOrNo
import matplotlib.pyplot as plt


exit = False
while not exit:
    base = read_excel()

    other = yesOrNo("Question of exam?")
    if other:
        exam(base["data"], base["headers"])
        break

    settings = questions_settings(base["headers"])

    for i in settings["qualitative"]:
        nominal = settings["qualitative"][i]
        t = create_table_qualitative(i, not nominal, base["data"], settings)

        print("\n Tabla de frecuencias de " + i)
        print(t)

        # Todo: Make Graph

    for i in settings["quantitative"]:
        discrete = settings["quantitative"][i]
        t = create_table_quantitative(i, discrete, base["data"], settings)

        print("\n Tabla de frecuencias de " + i)
        print(t)

        # Todo: Make Graph

    exit = yesOrNo("Desea salir?")
