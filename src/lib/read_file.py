from pandas import read_excel as pd_read_excel


def read_excel():
    print(
        "(Recuerda que la hoja del excel se debe llamar DB y tener la columna indice en la columna A)\nEscribe la ubicacion del excel a leer:"
    )
    path_file = input()

    base = pd_read_excel(path_file, sheet_name="DB", index_col=0, header=0)
    base_headers = list(base.columns.values)

    return {"data": base, "headers": base_headers}
