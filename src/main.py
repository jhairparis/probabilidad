from lib.read_file import read_excel
from lib.tables import create_table_qualitative, create_table_quantitative
from question import questions_settings
import matplotlib.pyplot as plt


base = read_excel()
settings = questions_settings(base["headers"])
print(settings)

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
