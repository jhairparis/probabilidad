from pandas import read_excel as pd_read_excel


def read_excel(path_file="src/files/BASE.xlsx"):
    base = pd_read_excel(path_file, sheet_name="DB", index_col=0, header=0)
    base_headers = list(base.columns.values)

    return {"data": base, "headers": base_headers}
